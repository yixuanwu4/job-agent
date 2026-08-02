<script setup lang="ts">
import type { ReportResponse } from '@/types'
import JobList from './JobList.vue'
import ReportSection from './ReportSection.vue'

defineProps<{
    report: ReportResponse
}>()
</script>

<template>
    <section>
        <h2>Matching Jobs</h2>
        <JobList :jobs="report.jobs" />
    </section>

    <ReportSection title="Skills Advice" :content="report.skills_advice" />
    <ReportSection title="Interview Preparation" :content="report.interview_prep" />
    <ReportSection title="Application Strategy" :content="report.application_strategy" />
</template>