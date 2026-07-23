from claude_client import call_agent


def get_skills_advice(jobs_text: str) -> str:
  return call_agent(
    "You are a career skills advisor. Based on the job listings above, "
    "which include a resume match score and missing keywords for each job, "
    "identify the most common skill gaps and suggest a brief learning path "
    "(what to study or build, roughly how long it takes) prioritized by which "
    "gaps show up most often across the lower-scoring jobs. "
    "Keep it under 300 words.",
    jobs_text,
  )


def get_interview_prep(jobs_text: str) -> str:
  return call_agent(
    "You are an interview coach. Based on the job listings above, generate "
    "3 likely interview questions for these roles, and briefly explain how "
    "to answer each one using the STAR method. For jobs with a lower resume "
    "match score, include a tip on how to address the missing keywords "
    "proactively during the interview. Keep it under 300 words.",
    jobs_text,
  )


def get_application_strategy(jobs_text: str) -> str:
  return call_agent(
    "You are a career strategist. Based on the job listings above, which are "
    "already ordered by resume match score from highest to lowest, suggest "
    "3-5 resume keywords to add (drawing from the missing_keywords across jobs) "
    "and confirm or adjust the application priority order with a one-line reason "
    "for each, referencing the match score where relevant. Keep it under 300 words.",
    jobs_text,
  )