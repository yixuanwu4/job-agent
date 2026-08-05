<script setup lang="ts">
import { ref } from 'vue'

const cv = ref<File | null>(null)
const role = ref('')
const location = ref('')
const country = ref('')
const preferred_language = ref('')
const sort_by = ref('score')

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
      preferred_language: string
      sort_by: string
    },
  ]
}>()

const handleSubmit = () => {
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
  <h1>Search Form</h1>
  <form @submit.prevent="handleSubmit">
    <div class="container">
      <label
        >Upload your CV (PDF or TXT)
        <input type="file" id="file" @change="get_cv" accept=".pdf, .txt" />
      </label>
      <label
        >Desired job titles (comma-separated, at least 3)
        <input type="text" v-model="role" placeholder="e.g. Frontend Developer, UI Engineer, Web Developer" />
      </label>
      <label
        >Location
        <input type="text" v-model="location" placeholder="e.g. London" />
      </label>
      <label
        >Country
        <input type="text" v-model="country" placeholder="e.g. United Kingdom" />
      </label>
      <label
        >Preferred job posting language
        <input type="text" v-model="preferred_language" placeholder="e.g. English" />
      </label>
      <label
        >Sort by
        <select id="sort-by" v-model="sort_by">
          <option value="score">Match score</option>
          <option value="date">Posting date</option>
        </select>
      </label>
      <button type="submit">Get my report</button>
    </div>
  </form>
</template>

<style>
.container {
  display: flex;
  flex-direction: column;
}
</style>
