<script setup lang="ts">
import type { ReportResponse } from '@/types'
import JobList from './JobList.vue'
import ReportSection from './ReportSection.vue'

defineProps<{
  report: ReportResponse
}>()
</script>

<template>
  <div class="report-results">
    <section class="jobs-section">
      <h2>Matching Jobs</h2>
      <JobList :jobs="report.jobs" />
    </section>

    <ReportSection title="Skills Advice" :content="report.skills_advice" />
    <ReportSection title="Interview Preparation" :content="report.interview_prep" />
    <ReportSection title="Application Strategy" :content="report.application_strategy" />
    <div class="logo">
      <a href="/">
        <img src="../../src/assets/job.png" />
      </a>
    </div>
  </div>
</template>

<style scoped>
.report-results {
  max-width: 720px;
  margin: 0 auto;
  padding: var(--space-6) var(--space-4);
}

.report-results > *:last-child {
  border-bottom: none;
}

.jobs-section h2 {
  font-size: var(--text-lg);
  margin-bottom: var(--space-4);
}

.logo {
  display: flex;
  flex-direction: column;
  width: 100%;
  align-items: center;
  margin-block: var(--space-4);
}

.logo a {
  width: 4rem;
  height: 4rem;
}
.logo img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  display: block;
}
</style>
