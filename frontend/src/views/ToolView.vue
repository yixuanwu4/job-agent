<script setup lang="ts">
import { ref } from 'vue'
import SearchForm from '@/components/SearchForm.vue'
import type { ReportResponse } from '@/types'
import ReportResults from '@/components/ReportResults.vue'

interface SearchPayload {
  cv: File | null
  role: string
  location: string
  country: string
  preferred_language: string
  sort_by: string
}

const report = ref<ReportResponse | null>(null)
const isLoading = ref(false)
const errorMessage = ref('')

async function handleSubmit(payload: SearchPayload) {
  if (!payload.cv) {
    errorMessage.value = 'Please upload your CV first.'
    isLoading.value = false
    return
  }

  isLoading.value = true
  errorMessage.value = ''
  report.value = null

  const url = 'https://job-agent-odvr.onrender.com/report'

  const formData = new FormData()
  formData.append('cv', payload.cv)
  formData.append('role', payload.role)
  formData.append('location', payload.location)
  formData.append('country', payload.country)
  formData.append('preferred_language', payload.preferred_language)
  formData.append('sort_by', payload.sort_by)

  try {
    const response = await fetch(url, { method: 'POST', body: formData })
    if (!response.ok) {
      throw new Error(response.statusText)
    }
    const data = await response.json()
    if (data.error) {
      errorMessage.value = data.error
      return
    }
    report.value = data
  } catch (error: unknown) {
    errorMessage.value = error instanceof Error ? error.message : 'Something went wrong.'
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="tool">
    <SearchForm @submit-search="handleSubmit" />

    <p v-if="isLoading">Generating your report... this can take up to a minute.</p>
    <p v-else-if="errorMessage">{{ errorMessage }}</p>
    <ReportResults v-else-if="report" :report="report" />
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
