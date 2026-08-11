# Job Agent

A job-search tool that matches your CV against live postings and tells you where you actually stand (a match score per listing), what's missing from your resume, and what to do about it.

## What it does

Upload a CV and a few job titles, and it pulls current listings from Adzuna, scores each one against your resume with Claude, and generates skill-gap advice, interview prep, and an application strategy. Use it once for an instant report, or subscribe for a short digest email each morning with anything new from the last 24 hours.

## Data

Two different paths, depending on how you use it:

- **One-off report** — your CV is read into memory, used to generate the report, and discarded. Nothing is written to a database or file storage.
- **Subscribing** — your email, CV, and search preferences are stored so the daily job has something to run against. There's no account or password; a unique link in each email lets you update your details or unsubscribe.
- **Unsubscribing deletes everything** — the database record and the CV file in storage are both removed, not deactivated or archived. There's nothing left afterward to delete a second time.

## For job seekers

- Every match comes with a score and the specific keywords your CV is missing for that listing
- Search multiple job titles at once (comma-separated), not just one exact phrase
- Filter by posting language, so listings you can't read don't show up
- Daily digests only include postings from the last 24 hours — no re-reading the same five listings every morning
- Skills advice, interview questions (STAR method), and an application priority order — generated from your actual matched jobs, not generic advice

## Running your own copy

This isn't a hosted product but something you can choose to deploy yourself, with your own accounts and API keys:

- **Anthropic** - job analysis
- **Adzuna** — job listings (free tier is shared per account and limited; multi-role searches use it up faster than you'd expect)
- **Supabase** — Postgres + file storage for subscriber data
- **Resend** — email, with your own verified sending domain

Cost scales with usage - a single report is typically a few cents in Claude API calls. Setup details are in `backend/` and `frontend/`.

## Known gaps

- No Imprint / Privacy Policy / Terms pages yet — needed before this is public-facing
- No rate limiting on the subscribe-link endpoint
- Job deduplication across multiple role searches works on title + company + description, which isn't perfect — near-identical postings can occasionally slip through