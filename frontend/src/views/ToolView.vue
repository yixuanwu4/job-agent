<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import SearchForm from '@/components/SearchForm.vue'
import SubscribeForm from '@/components/SubscribeForm.vue'
import { type SubscriberInfo, type ReportResponse } from '@/types'
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

const route = useRoute()
const subscriberInfo = ref<SubscriberInfo | null>(null)
const tokenError = ref('')

const isSubscribing = ref(false)
const subscribeError = ref('')
const subscribeSuccess = ref(false)

onMounted(async () => {
  const token = route.query.token as string
  if (!token) return

  const response = await fetch(
    `https://job-agent-odvr.onrender.com/subscriber-by-token?token=${token}`,
  )
  const data = await response.json()
  if (data.error) {
    tokenError.value = data.error
    return
  }
  subscriberInfo.value = data
})

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

async function handleSubscribeSubmit(payload: {
  cv: File | null
  email: string
  role: string
  location: string
  country: string
  preferred_language: string
}) {
  isSubscribing.value = true
  subscribeError.value = ''
  subscribeSuccess.value = false

  const url = 'https://job-agent-odvr.onrender.com/subscribe'

  const formData = new FormData()
  if (payload.cv) {
    formData.append('cv', payload.cv)
  }
  formData.append('email', payload.email)
  formData.append('role', payload.role)
  formData.append('location', payload.location)
  formData.append('country', payload.country)
  formData.append('preferred_language', payload.preferred_language)

  try {
    const response = await fetch(url, { method: 'POST', body: formData })
    if (!response.ok) {
      throw new Error(response.statusText)
    }
    const data = await response.json()
    if (data.error) {
      subscribeError.value = data.error
      return
    }
    subscribeSuccess.value = true
  } catch (error: unknown) {
    subscribeError.value = error instanceof Error ? error.message : 'Something went wrong.'
  } finally {
    isSubscribing.value = false
  }
}
</script>

<template>
  <div class="tool">
    <SearchForm v-if="!subscriberInfo" @submit-search="handleSubmit" />

    <SubscribeForm
      v-if="subscriberInfo"
      :initial-data="subscriberInfo"
      @submit-subscribe="handleSubscribeSubmit"
    />
    <p v-if="subscribeError">{{ subscribeError }}</p>
    <p v-if="subscribeSuccess">Your subscription has been updated!</p>

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
