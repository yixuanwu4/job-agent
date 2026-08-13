<script setup lang="ts">
import { onMounted, ref, computed, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import SearchForm from '@/components/SearchForm.vue'
import SubscribeForm from '@/components/SubscribeForm.vue'
import { type SubscriberInfo, type ReportResponse } from '@/types'
import ReportResults from '@/components/ReportResults.vue'
import RequestLinkForm from '@/components/RequestLinkForm.vue'
import LoadingState from '@/components/LoadingState.vue'
import { REPORT_LOADING_MESSAGES, SUBSCRIBE_LOADING_MESSAGES } from '@/constants.ts'

interface SearchPayload {
  cv: File | null
  role: string
  location: string
  country: string
  preferred_language: string
  sort_by: string
}

const API_BASE_URL = 'https://job-agent-odvr.onrender.com'

const report = ref<ReportResponse | null>(null)
const isLoading = ref(false)
const errorMessage = ref('')

const route = useRoute()
const subscriberInfo = ref<SubscriberInfo | null>(null)
const tokenError = ref('')
const subscribeMode = computed(() => route.query.mode === 'subscribe')

const currentView = computed(() => {
  if (isLoading.value) return 'loading-report'
  if (isSubscribing.value) return 'loading-subscribe'
  if (unsubscribed.value) return 'unsubscribed'
  if (report.value) return 'report'
  if (errorMessage.value) return 'report-error'
  if (subscribeSuccess.value) return 'subscribe-success'
  if (subscribeError.value) return 'subscribe-error'
  if (subscriberInfo.value) return 'subscribe-form'
  if (subscribeMode.value) return 'request-link'
  return 'search'
})

const isSubscribing = ref(false)
const subscribeError = ref('')
const subscribeSuccess = ref(false)

onMounted(async () => {
  const editToken = route.query.token as string
  const reportToken = route.query.report_token as string

  if (editToken) {
    const response = await fetch(`${API_BASE_URL}/subscriber-by-token?token=${editToken}`)
    const data = await response.json()
    if (data.error) {
      tokenError.value = data.error
      return
    }
    subscriberInfo.value = data
  }

  if (reportToken) {
    isLoading.value = true
    const response = await fetch(`${API_BASE_URL}/report-by-token?token=${reportToken}`)
    const data = await response.json()
    isLoading.value = false
    if (data.error) {
      errorMessage.value = data.error
      return
    }
    report.value = data
  }
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

  const url = `${API_BASE_URL}/report`

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
  role: string
  location: string
  country: string
  preferred_language: string
}) {
  isSubscribing.value = true
  subscribeError.value = ''
  subscribeSuccess.value = false

  const url = `${API_BASE_URL}/subscribe`
  const editToken = route.query.token as string

  const formData = new FormData()
  if (payload.cv) {
    formData.append('cv', payload.cv)
  }
  formData.append('token', editToken)
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

const isUnsubscribing = ref(false)
const unsubscribed = ref(false)
const router = useRouter()
const countdown = ref(3)

async function handleConfirmUnsubscribe() {
  isUnsubscribing.value = true
  const editToken = route.query.token as string

  const formData = new FormData()
  formData.append('token', editToken)

  try {
    const response = await fetch(`${API_BASE_URL}/unsubscribe`, {
      method: 'POST',
      body: formData,
    })
    const data = await response.json()
    if (data.error) {
      subscribeError.value = data.error
      return
    }
    unsubscribed.value = true
  } catch {
    subscribeError.value = 'Something went wrong. Please try again.'
  } finally {
    isUnsubscribing.value = false
  }
}

watch(unsubscribed, (isUnsubscribed) => {
  if (!isUnsubscribed) return
  const timer = setInterval(() => {
    countdown.value -= 1
    if (countdown.value <= 0) {
      clearInterval(timer)
      router.push('/')
    }
  }, 1000)
})
</script>

<template>
  <div class="tool">
    <SearchForm v-if="currentView === 'search'" @submit-search="handleSubmit" />
    <RequestLinkForm v-if="currentView === 'request-link'" />
    <SubscribeForm
      v-if="currentView === 'subscribe-form'"
      :initial-data="subscriberInfo"
      @submit-subscribe="handleSubscribeSubmit"
      @confirm-unsubscribe="handleConfirmUnsubscribe"
    />
    <div v-if="currentView === 'unsubscribed'">
      <h1>You've been unsubscribed</h1>
      <p>Redirecting to the homepage in {{ countdown }}...</p>
    </div>

    <LoadingState v-if="currentView === 'loading-report'" :messages="REPORT_LOADING_MESSAGES" />
    <LoadingState
      v-if="currentView === 'loading-subscribe'"
      :messages="SUBSCRIBE_LOADING_MESSAGES"
    />

    <p v-if="currentView === 'subscribe-error'">{{ subscribeError }}</p>
    <p v-if="currentView === 'subscribe-success'">Your subscription has been updated!</p>
    <p v-if="currentView === 'report-error'">{{ errorMessage }}</p>
    <ReportResults v-if="currentView === 'report'" :report="report!" />
  </div>
</template>
