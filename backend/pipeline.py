import os
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import requests

from language_detector import LanguageDetector


def filter_jobs_by_age(jobs: list[dict], max_age_days: int) -> list[dict]:
    cutoff = datetime.now(timezone.utc) - timedelta(days=max_age_days)
    filtered = []
    for j in jobs:
        try:
            posted = datetime.fromisoformat(j["posted_date"])
        except (ValueError, KeyError):
            continue
        if posted >= cutoff:
            filtered.append(j)
    return filtered

def format_date(iso_string: str) -> str:
    try:
        dt = datetime.fromisoformat(iso_string)
        dt_local = dt.astimezone(ZoneInfo("Europe/Zurich"))
        return dt_local.strftime("%Y-%m-%d %H:00")
    except ValueError:
        return "Unknown"

def parse_roles(role_string: str) -> list[str]:
    roles = [r.strip() for r in role_string.split(",") if r.strip()]
    if len(roles) < 3:
        raise ValueError("Please enter at least 3 job titles, separated by commas.")
    return roles

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


def get_matched_jobs_multi(roles: list[str], location: str, num_results: int, country: str, preferred_language: str) -> list[dict]:
    all_jobs = []
    seen = set()
    for role in roles:
        jobs = get_matched_jobs(role, location, num_results, country, preferred_language)
        for j in jobs:
            key = (j["title"], j["company"], j["description"])
            if key not in seen:
                seen.add(key)
                all_jobs.append(j)
    return all_jobs[:num_results]


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
