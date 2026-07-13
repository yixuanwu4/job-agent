import os
import requests
from datetime import datetime
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

JOB_ROLE = "Software Developer"
LOCATION = "ZURICH"
NUM_RESULTS = 10
COUNTRY = "ch"

client = Anthropic()
os.makedirs("outputs", exist_ok=True)

def get_jobs(role: str, location: str, num_results: int, country: str) -> list[dict]:
  app_id = os.environ["ADZUNA_APP_ID"]
  app_key = os.environ["ADZUNA_API_KEY"]
  url = f"https://api.adzuna.com/v1/api/jobs/{country}/search/1"
  params = {
    "app_id": app_id,
    "app_key": app_key,
    "results_per_page": num_results,
    "what": role,
    "where": location,
    "content-type": "application/json",
  }
  resp = requests.get(url, params = params, timeout = 20)
  resp.raise_for_status()
  data = resp.json()

  jobs = []
  for j in data.get("results", []):
    jobs.append({
      "title": j.get("title", "").strip(),
      "company": j.get("company", {}).get("display_name", "Unknown"),
      "location": j.get("location", {}).get("display_name", "Unknown"),
      "description": (j.get("description", "") or "")[:800],
      "url": j.get("redirect_url", ""),
    })
  return jobs

def call_agent(system_instructions: str, jobs_text: str) -> str:
  response = client.messages.create(
    model = "claude-haiku-4-5-20251001",
    max_tokens = 1500,
    system = f"Here is the list of jobs we searched for you:\n\n{jobs_text}",
    messages = [
      {"role": "user", "content": system_instructions}
    ]
  )
  # print(response.usage)
  text = "".join(block.text for block in response.content if block.type == "text")
  return text

def jobs_to_text(jobs: list[dict]) -> str:
  entries = []
  for i, j in enumerate(jobs, 1):
    entry = f"[Job {i}] {j['title']} @ {j['company']} ({j['location']})\n"
    entry += f"Description: {j['description']}\n"
    entry += f"Apply here: {j['url']}\n"
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

if __name__ == "__main__":
  jobs = get_jobs(JOB_ROLE, LOCATION, NUM_RESULTS, COUNTRY)
  jobs_text = jobs_to_text(jobs)

  skills = call_agent(
    "You are a career skills advisor. Based on the job listings above, "
    "list the most important skills required across these roles and suggest "
    "a brief learning path (what to study or build, roughly how long it takes). "
    "Keep it under 300 words.",
    jobs_text,
  )

  interview = call_agent(
    "You are an interview coach. Based on the job listings above, generate "
    "3 likely interview questions for these roles, and briefly explain how "
    "to answer each one using the STAR method. Keep it under 300 words.",
    jobs_text,
  )

  strategy = call_agent(
    "You are a career strategist. Based on the job listings above, suggest "
    "3-5 resume keywords to include, and rank the jobs by application priority "
    "with a one-line reason for each. Keep it under 300 words.",
    jobs_text,
  )

  report = build_report(jobs_text, skills, interview, strategy)
  file_name = os.path.join("outputs", "report_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt")
  with open(file_name, "w", encoding="utf-8") as f:
    f.write(report)