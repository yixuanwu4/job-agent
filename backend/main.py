import os
from datetime import datetime
from dotenv import load_dotenv

from pipeline import get_matched_jobs, jobs_to_text, build_report
from resume_analyzer import ResumeAnalyzer
from agents import get_skills_advice, get_interview_prep, get_application_strategy

load_dotenv()

JOB_ROLE = "Data Architect"
LOCATION = "ZURICH"
NUM_RESULTS = 10
COUNTRY = "ch"
PREFERRED_LANGUAGE = "english"

os.makedirs("outputs", exist_ok=True)


if __name__ == "__main__":
  jobs = get_matched_jobs(JOB_ROLE, LOCATION, NUM_RESULTS, COUNTRY, PREFERRED_LANGUAGE)

  analyzer = ResumeAnalyzer("cv.pdf")
  for j in jobs:
    match = analyzer.score_match(j["description"])
    j["match_score"] = match["score"]
    j["missing_keywords"] = match["missing_keywords"]

  jobs.sort(key=lambda j: j["match_score"], reverse=True)
  jobs_text = jobs_to_text(jobs)

  skills = get_skills_advice(jobs_text)
  interview = get_interview_prep(jobs_text)
  strategy = get_application_strategy(jobs_text)

  report = build_report(jobs_text, skills, interview, strategy)
  file_name = os.path.join("outputs", "report_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt")
  with open(file_name, "w", encoding="utf-8") as f:
    f.write(report)