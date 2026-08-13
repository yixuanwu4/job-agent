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
  <div class="subscribe" v-if="!sent">
    <h1>Enter your email to subscribe</h1>
    <form @submit.prevent="handleSubmit" class="container">
      <label
        >Email
        <input type="email" v-model="email" placeholder="e.g., abc@example.com" required />
      </label>
      <p class="form-hint">
        New here, or already subscribed? Either way, enter your email and we'll send you a unique
        link to update your details.
      </p>
      <button type="submit" :disabled="isSending">
        {{ isSending ? 'Sending...' : 'Send me a link' }}
      </button>
    </form>
  </div>
  <div class="hint">
    <p v-if="sent">
      Check your inbox 📧<br />We've sent a link to subscribe or update your details!
    </p>
  </div>
</template>

<style scoped>
.subscribe {
  display: flex;
  flex-direction: column;
  margin-block: var(--space-4);
  gap: var(--space-4);
}

h1 {
  margin-inline: var(--space-4);
}

.hint {
  display: flex;
  flex-direction: column;
  text-align: center;
}
</style>
