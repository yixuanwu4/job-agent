import os
import tempfile
from fastapi import FastAPI, UploadFile, Form

from pipeline import get_matched_jobs, sort_jobs, jobs_to_text
from resume_analyzer import ResumeAnalyzer
from agents import get_skills_advice, get_interview_prep, get_application_strategy

app = FastAPI()


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
        jobs = get_matched_jobs(
            role, location, num_results, country, preferred_language
        )
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
    except Exception as e:
        print(f"Error generating report: {e}")
        return {
            "error": "Something went wrong while generating your report. Please try again."
        }
    finally:
        if tmp_path:
            os.remove(tmp_path)
