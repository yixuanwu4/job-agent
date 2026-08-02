<script setup lang="ts">
import type { JobResult } from '@/types'
import JobCard from './JobCard.vue'

defineProps<{
  jobs: JobResult[]
}>()
</script>

<template>
  <div>
    <JobCard v-for="job in jobs" v-bind:key="job.url" :job="job" />
  </div>
</template>