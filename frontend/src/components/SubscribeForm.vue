<script setup lang="ts">
import { ref, watch } from 'vue'
import type { SubscriberInfo } from '@/types'

const props = defineProps<{
  initialData?: SubscriberInfo | null
}>()

const emit = defineEmits<{
  'submit-subscribe': [
    payload: {
      cv: File | null
      role: string
      location: string
      country: string
      preferred_language: string
    },
  ]
  'confirm-unsubscribe': []
}>()

const cv = ref<File | null>(null)
const role = ref('')
const location = ref('')
const country = ref('')
const preferred_language = ref('')
const showUnsubscribeConfirm = ref(false)

watch(
  () => props.initialData,
  (newData) => {
    if (newData) {
      country.value = newData?.country
      role.value = newData?.role
      location.value = newData?.location
      preferred_language.value = newData?.preferred_language
    }
  },
  { immediate: true },
)

function get_cv(event: Event) {
  const target = event.target as HTMLInputElement
  cv.value = target.files?.[0] ?? null
}

function handleSubmit() {
  emit('submit-subscribe', {
    cv: cv.value,
    role: role.value,
    location: location.value,
    country: country.value,
    preferred_language: preferred_language.value,
  })
}
</script>

<template>
  <div class="tool">
    <h1>Hello {{ initialData?.email }}</h1>
    <p class="form-intro">Fill in or update your job search details below.</p>
    <form @submit.prevent="handleSubmit">
      <div class="container">
        <label
          >Update your CV (optional — leave empty to keep your current one)
          <input type="file" id="file" @change="get_cv" accept=".pdf, .txt" />
        </label>
        <label
          >Update desired job titles (comma-separated, at least 3)
          <input
            type="text"
            v-model="role"
            placeholder="e.g. Frontend Developer, UI Engineer, Web Developer"
          />
        </label>
        <label
          >Update location
          <input type="text" v-model="location" placeholder="e.g. London" />
        </label>
        <label
          >Update country
          <input type="text" v-model="country" placeholder="e.g. United Kingdom" />
        </label>
        <label
          >Update preferred job posting language
          <input type="text" v-model="preferred_language" placeholder="e.g. English" />
        </label>
        <button type="submit">Update my information</button>
      </div>
    </form>
    <div class="unsubscribe-section">
      <button
        v-if="!showUnsubscribeConfirm"
        type="button"
        class="text-link"
        @click="showUnsubscribeConfirm = true"
      >
        Unsubscribe
      </button>

      <div v-else class="unsubscribe-confirm">
        <p>
          This will permanently delete your email, CV, and search preferences. This cannot be
          undone.
        </p>
        <button type="button" @click="emit('confirm-unsubscribe')">Yes, delete my data</button>
        <button type="button" class="text-link" @click="showUnsubscribeConfirm = false">
          Cancel
        </button>
      </div>
    </div>
  </div>
</template>
