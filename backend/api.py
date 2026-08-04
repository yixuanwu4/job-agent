import os
import tempfile

from fastapi import FastAPI, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from agents import get_application_strategy, get_interview_prep, get_skills_advice
from countries import get_country_code
from pipeline import (
    get_matched_jobs_multi,
    jobs_to_text,
    parse_roles,
    sort_jobs,
)
from resume_analyzer import ResumeAnalyzer
from supabase_client import (
    add_subscriber,
    download_cv,
    get_subscriber_by_token,
    upload_cv,
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://yixuanwu4.github.io",
        "http://localhost:5173",
        ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/report")
async def generate_report(
    cv: UploadFile,
    role: str = Form(...),
    location: str = Form(...),
    country: str = Form(...),
    preferred_language: str = Form(...),
    sort_by: str = Form("match_score"),
    num_results: int = Form(10),
):
    tmp_path = None
    try:
        cv_bytes = await cv.read()
        suffix = os.path.splitext(cv.filename)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(cv_bytes)
            tmp_path = tmp.name

        country_code = get_country_code(country)
        roles = parse_roles(role)
        jobs = get_matched_jobs_multi(roles, location, num_results, country_code, preferred_language)

        analyzer = ResumeAnalyzer(tmp_path)
        for j in jobs:
            match = analyzer.score_match(j["description"])
            j["match_score"] = match["score"]
            j["missing_keywords"] = match["missing_keywords"]

        jobs = sort_jobs(jobs, sort_by)
        jobs_text = jobs_to_text(jobs)

        skills = get_skills_advice(jobs_text)
        interview = get_interview_prep(jobs_text)
        strategy = get_application_strategy(jobs_text)

        return {
            "jobs": jobs,
            "skills_advice": skills,
            "interview_prep": interview,
            "application_strategy": strategy,
        }
    except ValueError as e:
        print(f"Error finding target country: {e}")
        return {"error": str(e)}
    except Exception as e:
        print(f"Error generating report: {e}")
        return {
            "error": "Something went wrong while generating your report. Please try again."
        }
    finally:
        if tmp_path:
            os.remove(tmp_path)


@app.post("/subscribe")
async def create_subscription(
    cv: UploadFile,
    role: str = Form(...),
    location: str = Form(...),
    country: str = Form(...),
    preferred_language: str = Form(...),
    email: str = Form(...),
):
    try:
        cv_bytes = await cv.read()
        file_name = cv.filename
        cv_storage_path = upload_cv(cv_bytes, file_name, email)
        country_code = get_country_code(country)
        parse_roles(role)
        add_subscriber(
            email,
            role,
            location,
            country_code,
            preferred_language,
            cv_storage_path,
        )

        print("Subscribed!")
        return {"status": "subscribed", "email": email}
    except ValueError as e:
        print(f"Validation error in /subscribe: {e}")
        return {"error": str(e)}
    except Exception as e:
        print(f"Error subscribing our website: {e}")
        return {"error": "Something went wrong while subscribing. Please try again."}

@app.get("/report-by-token")
async def get_report_by_token(token: str):
    subscriber = get_subscriber_by_token(token)
    if subscriber is None:
        return {"error": "This link is no longer valid."}

    tmp_path = None
    try:
        cv_bytes = download_cv(subscriber["cv_storage_path"])
        suffix = os.path.splitext(subscriber["cv_storage_path"])[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(cv_bytes)
            tmp_path = tmp.name

        roles = parse_roles(subscriber["role"])
        jobs = get_matched_jobs_multi(
            roles, subscriber["location"], 10, subscriber["country"], subscriber["preferred_language"],
        )

        analyzer = ResumeAnalyzer(tmp_path)
        for j in jobs:
            match = analyzer.score_match(j["description"])
            j["match_score"] = match["score"]
            j["missing_keywords"] = match["missing_keywords"]

        jobs = sort_jobs(jobs, "match_score")
        jobs_text = jobs_to_text(jobs)

        skills = get_skills_advice(jobs_text)
        interview = get_interview_prep(jobs_text)
        strategy = get_application_strategy(jobs_text)

        return {
            "jobs": jobs,
            "skills_advice": skills,
            "interview_prep": interview,
            "application_strategy": strategy
        }
    except Exception as e:
        print(f"Error generating report by token: {e}")
        return {"error": "Something went wrong while generating your report."}
    finally: 
        if tmp_path:
            os.remove(tmp_path)