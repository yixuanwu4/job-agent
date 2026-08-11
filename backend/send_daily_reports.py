import os
import tempfile

from email_client import send_email
from email_template import build_digest_html, build_digest_text
from pipeline import filter_jobs_by_age, get_matched_jobs_multi, parse_roles, sort_jobs
from resume_analyzer import ResumeAnalyzer
from supabase_client import download_cv, get_active_subscribers

REPORT_BASE_URL = "https://yixuanwu4.github.io/job-agent/tool"

def process_subscriber(subscriber: dict):
    tmp_path = None
    try:
        cv_bytes = download_cv(subscriber["cv_storage_path"])
        suffix = os.path.splitext(subscriber["cv_storage_path"])[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(cv_bytes)
            tmp_path = tmp.name

        roles = parse_roles(subscriber["role"])
        jobs = get_matched_jobs_multi(
            roles, subscriber["location"], 50,
            subscriber["country"], subscriber["preferred_language"],
        )
        jobs = filter_jobs_by_age(jobs, max_age_days=1)
        print(f"After 24h filter: {len(jobs)} jobs")

        if not jobs:
            print(f"No jobs found for {subscriber['email']}, skipping email.")
            return

        analyzer = ResumeAnalyzer(tmp_path)
        for j in jobs:
            match = analyzer.score_match(j["description"])
            j["match_score"] = match["score"]
        jobs = sort_jobs(jobs, "match_score")

        report_url = f"{REPORT_BASE_URL}?report_token={subscriber['token']}"
        manage_url = f"{REPORT_BASE_URL}?token={subscriber['token']}"
        html = build_digest_html(jobs, report_url, manage_url)
        text = build_digest_text(jobs, report_url, manage_url)
        send_email (subscriber["email"], f"{len(jobs)} new job matches today", html, text)
        print(f"Sent to {subscriber['email']}")

    except Exception as e:
        print(f"Failed to process {subscriber['email']}: {e}")
    finally:
        if tmp_path:
            os.remove(tmp_path)

def main():
    subscribers = get_active_subscribers()
    print(f"Processing {len(subscribers)} subscribers...")
    for sub in subscribers:
        process_subscriber(sub)

if __name__ == "__main__":
    main()