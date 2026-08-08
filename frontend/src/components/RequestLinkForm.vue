<script setup lang="ts">
import { ref } from 'vue'

const email = ref('')
const isSending = ref(false)
const sent = ref(false)
const error = ref('')

async function handleSubmit() {
  isSending.value = true
  error.value = ''

  const formData = new FormData()
  formData.append('email', email.value)

  try {
    const response = await fetch('https://job-agent-odvr.onrender.com/request-subscribe-link', {
      method: 'POST',
      body: formData,
    })
    const data = await response.json()
    if (data.error) {
      error.value = data.error
      return
    }
    sent.value = true
  } catch {
    error.value = 'Something went wrong. Please try again.'
  } finally {
    isSending.value = false
  }
}
</script>

<template>
    <h1>Enter your email to subscribe</h1>
  <form v-if="!sent" @submit.prevent="handleSubmit" class="container">
    <label
      >Email
      <input type="email" v-model="email" placeholder="e.g., abc@example.com" required />
    </label>
    <button type="submit" :disabled="isSending">
      {{ isSending ? 'Sending...' : 'Send me a link' }}
    </button>
  </form>
  <h1 v-if="sent">You have successfully subscribed now. Please check your email box.</h1>
</template>
