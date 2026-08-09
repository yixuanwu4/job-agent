<script setup lang="ts">
import type { JobResult } from '@/types'
import JobCard from './JobCard.vue'

defineProps<{
  jobs: JobResult[]
}>()
</script>

<template>
  <div class="job-list">
    <JobCard v-for="job in jobs" v-bind:key="job.url" :job="job" />
  </div>
</template>

<style scoped>
.job-list {
  border: 1px solid var(--color-border);
  border-radius: var(--radius-card);
  overflow: hidden;
}
</style>
