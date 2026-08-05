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
      email: string
      role: string
      location: string
      country: string
      preferred_language: string
    },
  ]
}>()

const cv = ref<File | null>(null)
const email = ref('')
const role = ref('')
const location = ref('')
const country = ref('')
const preferred_language = ref('')

watch(
  () => props.initialData,
  (newData) => {
    if (newData) {
      country.value = newData?.country
      email.value = newData?.email
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
    email: email.value,
    role: role.value,
    location: location.value,
    country: country.value,
    preferred_language: preferred_language.value,
  })
}
</script>

<template>
  <h1>Subscriber Information</h1>
  <form @submit.prevent="handleSubmit">
    <div class="container">
      <label
        >Update your CV (PDF or TXT)
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
      <label
        >Email
        <input type="email" v-model="email" placeholder="e.g., abc@example.com" />
      </label>
      <button type="submit">Update my information</button>
    </div>
  </form>
</template>
