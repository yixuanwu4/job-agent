from pypdf import PdfReader
import json
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
        "Compare this resume against the job description below. "
        "Respond with ONLY valid JSON in this exact format, no other text:\n"
        '{"score": <integer 0-100>, "missing_keywords": ["keyword1", "keyword2"]}\n\n'
        f"Job description:\n{job_description}"
    )
    result = call_agent(prompt, self.resume_text)
    
    cleaned = result.strip()
    if cleaned.startswith("```"):
      cleaned = cleaned.strip("`")
      cleaned = cleaned.removeprefix("json").strip()

    try:
      return json.loads(cleaned)
    except json.JSONDecodeError:
      print(repr(result))
      return {"score": 0, "missing_keywords": []}