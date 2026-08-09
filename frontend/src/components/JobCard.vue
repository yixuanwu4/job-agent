<script setup lang="ts">
import type { JobResult } from '@/types'

defineProps<{
  job: JobResult
}>()

function formatDate(iso: string): string {
  try {
    return new Date(iso).toLocaleDateString('en-GB', { day: 'numeric', month: 'short' })
  } catch {
    return ''
  }
}
</script>

<template>
  <div class="job-card">
    <div class="job-card-main">
      <div class="job-card-header">
        <h3>{{ job.title }}</h3>
        <div class="job-meta">
          <span>{{ job.company }}</span>
          <span class="dot">·</span>
          <span>{{ job.location }}</span>
          <span class="dot">·</span>
          <span>{{ formatDate(job.posted_date) }}</span>
        </div>
      </div>
      <p class="job-description">{{ job.description }}</p>
      <div class="missing-keywords" v-if="job.missing_keywords.length">
        <span class="missing-keywords-label">Missing:</span>
        <span v-for="word in job.missing_keywords" :key="word" class="keyword-pill">{{
          word
        }}</span>
      </div>
      <a :href="job.url" target="_blank" class="job-link">View job →</a>
    </div>

    <div class="job-card-score">
      <svg viewBox="0 0 40 40" class="score-ring">
        <circle cx="20" cy="20" r="17" class="score-ring-track" />
        <circle
          cx="20"
          cy="20"
          r="17"
          class="score-ring-fill"
          pathLength="1"
          :style="{
            strokeDashoffset: 1 - job.match_score / 100,
            opacity: 0.4 + (job.match_score / 100) * 0.6,
          }"
        />
      </svg>
      <span class="score-value">{{ job.match_score }}</span>
    </div>
  </div>
</template>

<style scoped>
.job-card {
  display: flex;
  justify-content: space-between;
  gap: var(--space-5);
  padding: var(--space-5);
  border-bottom: 1px dashed var(--color-border);
}

.job-card:last-child {
  border-bottom: none;
}

.job-card-main {
  flex: 1;
  min-width: 0;
}

.job-card-header h3 {
  font-size: var(--text-base);
  font-weight: 600;
  margin-bottom: var(--space-1);
}

.job-meta {
  font-size: var(--text-sm);
  color: var(--color-text-muted);
  display: flex;
  gap: var(--space-2);
  margin-bottom: var(--space-3);
}

.job-description {
  font-size: var(--text-sm);
  color: var(--color-text-muted);
  line-height: 1.6;
  margin-bottom: var(--space-3);
  display: -webkit-box;
  line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.missing-keywords-label {
  font-size: var(--text-sm);
  color: var(--color-text-muted);
  margin-right: var(--space-1);
}

.missing-keywords {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
  margin-bottom: var(--space-3);
}

.keyword-pill {
  font-size: var(--text-sm);
  font-family: var(--font-mono);
  color: var(--color-text);
  background: var(--raw-grey);
  border-radius: var(--radius-pill);
  padding: 2px var(--space-3);
}

.job-link {
  font-size: var(--text-sm);
  font-weight: 600;
}

.job-card-score {
  position: relative;
  flex-shrink: 0;
  width: 56px;
  height: 56px;
}

.score-ring {
  width: 100%;
  height: 100%;
  transform: rotate(-90deg);
}

.score-ring-track {
  fill: none;
  stroke: var(--color-accent-soft);
  stroke-width: 3;
}

.score-ring-fill {
  fill: none;
  stroke: var(--color-text-muted);
  stroke-width: 4;
  stroke-linecap: round;
  stroke-dasharray: 1;
  transition: stroke-dashoffset 0.6s ease;
}

.score-value {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-family: var(--font-mono);
  font-size: var(--text-sm);
  font-weight: 500;
}
</style>
