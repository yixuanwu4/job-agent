# Job Search Agent

A lightweight, multi-agent job search assistant. It pulls live job listings, scores them against your resume, and generates a personalized report covering skill gaps, interview prep, and application strategy — all ranked by how well each job actually fits you.

Built with direct Anthropic API calls (no agent framework), keeping it fast, simple to debug, and cheap to run — typically a few cents per search using Claude Haiku 4.5.

## Features

- **Live job search** via the Adzuna API
- **Resume matching**: parses your CV (PDF or TXT) and scores each job against it (0–100), with a list of missing keywords per job
- **Automatic ranking**: jobs are sorted highest-match first
- **Three specialist analyses** per search, grounded in your actual results:
  - **Skills advisor** — key skill gaps and a brief learning path
  - **Interview coach** — likely interview questions with STAR-method answer guidance
  - **Career strategist** — resume keyword suggestions and application priority order
- **Timestamped report** saved to `outputs/` as a plain text file

## How it works

```
get_jobs()              → pull listings from Adzuna
ResumeAnalyzer           → score + missing keywords per job (via Claude)
jobs.sort()               → rank by match score
jobs_to_text()          → format listings + scores for the agents
call_agent() × 3        → skills / interview / strategy analysis
build_report()          → assemble everything into one report
                         → written to outputs/report_<timestamp>.txt
```

## Project structure

```
job-agent/
├── main.py              # orchestrates the full pipeline
├── claude_client.py     # single reusable function for calling the Claude API
├── resume_analyzer.py   # ResumeAnalyzer class: reads CV, scores against jobs
├── cv.pdf / cv.txt       # your resume (not committed — see Setup)
├── .env                  # API keys (not committed)
└── outputs/               # generated reports land here
```

## Setup

### 1. Get API keys

- **Anthropic API key** — from [console.anthropic.com](https://console.anthropic.com/). New accounts get some free credit; usage on this project is a few cents per run.
- **Adzuna API key** — free, from [developer.adzuna.com](https://developer.adzuna.com/). Free tier is 250 calls/month, plenty for personal use. You'll get an App ID and an API key.

### 2. Install dependencies

```bash
pip install anthropic requests python-dotenv pypdf
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```
ANTHROPIC_API_KEY=sk-ant-your-key-here
ADZUNA_APP_ID=your-app-id
ADZUNA_API_KEY=your-adzuna-key
```

### 4. Add your resume

Place a `cv.pdf` or `cv.txt` in the project root (or update the path passed to `ResumeAnalyzer(...)` in `main.py`).

### 5. Set your search parameters

At the top of `main.py`:

```python
JOB_ROLE = "Software Developer"
LOCATION = "ZURICH"
NUM_RESULTS = 10
COUNTRY = "ch"          # Adzuna country code, e.g. "us", "gb", "de", "ch"
```

## Usage

```bash
python main.py
```

This will:
1. Fetch job listings matching your search
2. Score each one against your resume
3. Sort them by match score
4. Run the three analysis agents
5. Save a full report to `outputs/report_<timestamp>.txt`

## Cost

At this project's scale (≤10 jobs, Claude Haiku 4.5), a full run — including resume scoring for every job plus the three analysis agents — typically costs a few cents. Note: prompt caching was evaluated for this project but doesn't help here, since job description snippets from Adzuna's free tier are far below the minimum token threshold required to trigger it.

## Next steps

- **Language filtering**: automatically exclude listings that aren't in English, or that require fluent German — not yet implemented, planned as a pre-filter step right after `get_jobs()` (before resume scoring, to save on API calls for jobs you'd skip anyway)
- CLI arguments (`--role`, `--location`) instead of editing constants in `main.py`
- Track previously seen job URLs across runs to avoid re-analyzing the same listings
- Optional PDF export of the report

## Notes

- Adzuna's free search endpoint returns a short description snippet (~500 characters), not the full posting — resume match scores and skill analysis are based on that snippet, not the complete job ad.
- Language detection and German-requirement filtering (see Next steps) will further reduce noise once added.