<script setup lang="ts">
import { ref } from 'vue'
import LanguagePicker from './LanguagePicker.vue'
import { SUPPORTED_LANGUAGES } from '@/constants.ts'

const cv = ref<File | null>(null)
const role = ref('')
const location = ref('')
const country = ref('')
const preferred_language = ref<string[]>([])
const sort_by = ref('score')

const fieldErrors = ref<Record<string, string>>({})

function validate(): boolean {
  const errors: Record<string, string> = {}

  if (!cv.value) {
    errors.cv = 'Please upload your CV.'
  }

  const roleCount = role.value
    .split(',')
    .map((r) => r.trim())
    .filter(Boolean).length

  if (roleCount < 3) {
    errors.role = 'Enter at least 3 job titles, separated by commas.'
  }

  if (!location.value.trim()) {
    errors.location = 'Location is required.'
  }

  if (!country.value.trim()) {
    errors.country = 'Country is required.'
  }

  if (preferred_language.value.length === 0) {
    errors.preferred_language = 'Select at least one language.'
  }

  fieldErrors.value = errors
  return Object.keys(errors).length === 0
}

function get_cv(event: Event) {
  const target = event.target as HTMLInputElement
  cv.value = target.files?.[0] ?? null
}

const emit = defineEmits<{
  'submit-search': [
    payload: {
      cv: File | null
      role: string
      location: string
      country: string
      preferred_language: string[]
      sort_by: string
    },
  ]
}>()

function handleSubmit() {
  if (!validate()) return

  emit('submit-search', {
    cv: cv.value,
    role: role.value,
    location: location.value,
    country: country.value,
    preferred_language: preferred_language.value,
    sort_by: sort_by.value,
  })
}
</script>

<template>
  <div class="tool">
    <h1>Search Form</h1>

    <form @submit.prevent="handleSubmit">
      <div class="container">
        <label>
          Upload your CV (PDF or TXT)
          <input
            id="file"
            type="file"
            accept=".pdf, .txt"
            @change="get_cv"
          />
          <span v-if="fieldErrors.cv" class="field-error">
            {{ fieldErrors.cv }}
          </span>
        </label>

        <label>
          Desired job titles (comma-separated, at least 3)
          <input
            v-model="role"
            type="text"
            placeholder="e.g. Frontend Developer, UI Engineer, Web Developer"
          />
          <span v-if="fieldErrors.role" class="field-error">
            {{ fieldErrors.role }}
          </span>
        </label>

        <label>
          Location
          <input
            v-model="location"
            type="text"
            placeholder="e.g. London"
          />
          <span v-if="fieldErrors.location" class="field-error">
            {{ fieldErrors.location }}
          </span>
        </label>

        <label>
          Country
          <select v-model="country">
            <option value="" disabled>Select a country</option>
            <option value="Switzerland">Switzerland</option>
            <option value="Norway">Norway</option>
            <option value="Sweden">Sweden</option>
            <option value="United Kingdom">United Kingdom</option>
            <option value="Netherlands">Netherlands</option>
            <option value="Belgium">Belgium</option>
            <option value="Germany">Germany</option>
            <option value="Austria">Austria</option>
            <option value="France">France</option>
            <option value="Italy">Italy</option>
            <option value="Portugal">Portugal</option>
            <option value="Spain">Spain</option>
          </select>
          <span v-if="fieldErrors.country" class="field-error">
            {{ fieldErrors.country }}
          </span>
        </label>

        <label>
          Preferred job posting language

          <LanguagePicker v-model="preferred_language" :options=SUPPORTED_LANGUAGES
          />

          <span v-if="fieldErrors.preferred_language" class="field-error">
            {{ fieldErrors.preferred_language }}
          </span>
        </label>

        <label>
          Sort by
          <select id="sort-by" v-model="sort_by">
            <option value="score">Match score</option>
            <option value="date">Posting date</option>
          </select>
        </label>

        <button type="submit">Get my report</button>
      </div>
    </form>
  </div>
</template>

<style>
.container {
  display: flex;
  flex-direction: column;
}
</style>