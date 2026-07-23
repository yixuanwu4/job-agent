import os
import requests
from language_detector import LanguageDetector
from datetime import datetime
from zoneinfo import ZoneInfo


def format_date(iso_string: str) -> str:
    try:
        dt = datetime.fromisoformat(iso_string)
        dt_local = dt.astimezone(ZoneInfo("Europe/Zurich"))
        return dt_local.strftime("%Y-%m-%d %H:00")
    except ValueError:
        return "Unknown"


def get_matched_jobs(
    role: str, location: str, num_results: int, country: str, preferred_language: str
) -> list[dict]:
    fetch_count = 50  # Adzuna max fetch number
    app_id = os.environ["ADZUNA_APP_ID"]
    app_key = os.environ["ADZUNA_API_KEY"]
    url = f"https://api.adzuna.com/v1/api/jobs/{country}/search/1"
    params = {
        "app_id": app_id,
        "app_key": app_key,
        "results_per_page": fetch_count,
        "what": role,
        "where": location,
        "content-type": "application/json",
    }
    resp = requests.get(url, params=params, timeout=20)
    resp.raise_for_status()
    data = resp.json()

    jobs = []
    for j in data.get("results", []):
        jobs.append(
            {
                "title": j.get("title", "").strip(),
                "company": j.get("company", {}).get("display_name", "Unknown"),
                "location": j.get("location", {}).get("display_name", "Unknown"),
                "description": (j.get("description", "") or "")[:800],
                "url": j.get("redirect_url", ""),
                "posted_date": j.get("created", ""),
            }
        )
    detector = LanguageDetector(preferred_language)
    jobs = detector.filter_jobs_by_language(jobs)
    return jobs[:num_results]


def sort_jobs(jobs: list[dict], sort_by: str = "match_score") -> list[dict]:
    if sort_by == "date":
        return sorted(jobs, key=lambda j: j["posted_date"], reverse=True)
    return sorted(jobs, key=lambda j: j["match_score"], reverse=True)


def jobs_to_text(jobs: list[dict]) -> str:
    entries = []
    for i, j in enumerate(jobs, 1):
        entry = f"[Job {i}] {j['title']} @ {j['company']} ({j['location']})\n"
        entry += f"\nPosted: {format_date(j['posted_date'])}\n"
        entry += f"\nDescription: {j['description']}\n"
        entry += f"\nMatching score: {j['match_score']}\n"
        entry += f"\nMissing keywords: {j['missing_keywords']}\n"
        entry += f"\nApply here: {j['url']}\n"
        entries.append(entry)
    return "\n".join(entries)


def build_report(jobs_text: str, skills: str, interview: str, strategy: str) -> str:
    all_content = (
        "--------------------JOBS LIST--------------------\n"
        + jobs_text
        + "\n--------------------SKILLS ADVISOR--------------------\n"
        + skills
        + "\n--------------------INTERVIEW PREPERATION--------------------\n"
        + interview
        + "\n--------------------APPLICATION STRATEGY--------------------\n"
        + strategy
    )
    return all_content
