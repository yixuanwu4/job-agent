<script setup lang="ts">
import type { JobResult } from '@/types'

defineProps<{
    job: JobResult
}>()
</script>

<template>
    <div class="job-card">
        <h2>{{ job.title }}</h2>
        <div class="job-meta">
            <h3>{{ job.company }}</h3>
            <h4>{{ job.location }}</h4>
            <h4>{{ job.posted_date }}</h4>
        </div>
        <div class="job-details">
            <div class="job-col1">
                <p>{{ job.description }}</p>
            </div>
            <div class="job-col2">
                <p>{{ job.match_score }}</p>
                <p class="missing-key-words" v-for="word in job.missing_keywords" v-bind:key="job.url+'/'+word">{{ word }}</p>
                <a target="_blank" :href="job.url">View job</a>
            </div>    
        </div>
    </div>
</template>