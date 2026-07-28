import json

from pypdf import PdfReader

from claude_client import call_agent


class ResumeAnalyzer:
  def __init__(self, resume_path: str):
    self.resume_path = resume_path
    self.resume_text = self.read_resume(resume_path)

  def read_resume(self, path: str) -> str:
    text = ""
    if self.resume_path.endswith(".txt"):
      with open(path, encoding="utf-8") as f:
        text = f.read()
    elif self.resume_path.endswith(".pdf"):
      reader = PdfReader(path)
      for page in reader.pages:
        text += page.extract_text()
    else:
      raise ValueError(f"Unsupported file type: {path}")
    return text

  def score_match(self, job_description: str) -> dict:
    prompt = (
        "Extract the key skills, qualifications, and requirements from this "
        "job description. For each one, decide whether the resume below "
        "demonstrates it. Count it as matched if the resume shows equivalent "
        "or related experience, even if the exact wording differs — for "
        "example, 'data pipeline' experience should satisfy an 'ETL' "
        "requirement, and a 'Data Analyst' background with architecture-level "
        "work should satisfy a 'Data Architect' requirement. Judge substance, "
        "not exact phrasing.\n\n"
        "Respond with ONLY valid JSON in this exact format, no other text, "
        "no markdown code blocks:\n"
        '{"keyword_checks": [{"keyword": "...", "matched": true, '
        '"reason": "brief reason"}, ...]}\n\n'
        f"Job description:\n{job_description}"
    )
    result = call_agent(prompt, self.resume_text)

    cleaned = result.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.strip("`")
        cleaned = cleaned.removeprefix("json").strip()

    try:
        parsed = json.loads(cleaned)
    except json.JSONDecodeError:
        return {"score": 0, "missing_keywords": []}

    checks = parsed.get("keyword_checks", [])
    total = len(checks)
    matched_count = sum(1 for c in checks if c.get("matched"))
    missing_keywords = [c["keyword"] for c in checks if not c.get("matched")]

    score = round((matched_count / total) * 100) if total > 0 else 0

    return {"score": score, "missing_keywords": missing_keywords}