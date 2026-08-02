export interface JobResult {
    title: string
    company: string
    location: string
    description: string
    url: string
    posted_date: string
    match_score: number
    missing_keywords: string[]
}

export interface ReportResponse {
    jobs: JobResult[]
    skills_advice: string
    interview_prep: string
    application_strategy: string
}