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

const fieldErrors = ref<Record<string, string>>({})

function validate(): boolean {
  const errors: Record<string, string> = {}

  if (!cv.value && !props.initialData?.has_cv) {
    console.log(props.initialData?.has_cv)
    errors.cv = 'Please upload your CV.'
  }

  if (role.value == null) {
    errors.role = 'Enter at least 3 job titles, separated by commas.'
  } else {
    const roleCount = role.value
      .split(',')
      .map((r) => r.trim())
      .filter(Boolean).length
    if (roleCount < 3) {
      errors.role = 'Enter at least 3 job titles, separated by commas.'
    }
  }

  if (location.value == null || !location.value.trim()) {
    errors.location = 'Location is required.'
  }

  if (country.value == null || !country.value.trim()) {
    errors.country = 'Country is required.'
  }

  if (preferred_language.value == null || !preferred_language.value.trim()) {
    errors.preferred_language = 'Preferred language is required.'
  }

  fieldErrors.value = errors
  return Object.keys(errors).length == 0
}

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
  if (!validate()) return

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
          <span v-if="fieldErrors.cv" class="field-error">{{ fieldErrors.cv }}</span>
        </label>
        <label
          >Update desired job titles (comma-separated, at least 3)
          <input
            type="text"
            v-model="role"
            placeholder="e.g. Frontend Developer, UI Engineer, Web Developer"
          />
          <span v-if="fieldErrors.role" class="field-error">{{ fieldErrors.role }}</span>
        </label>
        <label
          >Update location
          <input type="text" v-model="location" placeholder="e.g. London" />
          <span v-if="fieldErrors.location" class="field-error">{{ fieldErrors.location }}</span>
        </label>
        <label
          >Update country
          <input type="text" v-model="country" placeholder="e.g. United Kingdom" />
          <span v-if="fieldErrors.country" class="field-error">{{ fieldErrors.country }}</span>
        </label>
        <label
          >Update preferred job posting language
          <input type="text" v-model="preferred_language" placeholder="e.g. English" />
          <span v-if="fieldErrors.preferred_language" class="field-error">{{
            fieldErrors.preferred_language
          }}</span>
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
        <button type="button" class="btn-danger" @click="emit('confirm-unsubscribe')">
          Yes, delete my data
        </button>
        <button type="button" class="text-link" @click="showUnsubscribeConfirm = false">
          Cancel
        </button>
      </div>
    </div>
  </div>
</template>

<style>
.unsubscribe-section {
  margin-top: var(--space-6);
  padding-top: var(--space-5);
  text-align: center;
}

.text-link {
  background: none;
  border: none;
  color: var(--color-text-muted);
  font-size: var(--text-sm);
  text-decoration: underline;
  cursor: pointer;
  padding: 0;
}

.text-link:hover {
  color: var(--color-text);
}

.unsubscribe-confirm p {
  font-size: var(--text-sm);
  color: var(--color-text-muted);
  margin-bottom: var(--space-3);
}

.unsubscribe-confirm {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  align-items: center;
}

.btn-danger {
  background: var(--color-danger);
  color: var(--raw-paper);
  border: none;
  height: 1.6rem;
}
</style>
