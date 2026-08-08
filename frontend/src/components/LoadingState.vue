<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch } from 'vue'

const props = defineProps<{
  messages: string[]
}>()

const currentIndex = ref(0)
const currentMessage = ref(props.messages[0])

let intervalId: ReturnType<typeof setInterval> | undefined

function startCycle() {
  stopCycle()
  currentIndex.value = 0
  currentMessage.value = props.messages[0] ?? ''

  if (props.messages.length <= 1) return

  intervalId = setInterval(() => {
    currentIndex.value = (currentIndex.value + 1) % props.messages.length
    currentMessage.value = props.messages[currentIndex.value]
  }, 3200)
}

function stopCycle() {
  if (intervalId) {
    clearInterval(intervalId)
    intervalId = undefined
  }
}

onMounted(startCycle)
onUnmounted(stopCycle)

watch(() => props.messages, startCycle)
</script>

<template>
  <div class="loading-state">
    <svg class="briefcase" viewBox="0 0 64 64" fill="none">
      <path
        pathLength="1"
        d="M20 24 V18 a4 4 0 0 1 4 -4 h16 a4 4 0 0 1 4 4 V24 M8 24 h48 v26 a4 4 0 0 1 -4 4 H12 a4 4 0 0 1 -4 -4 Z M8 36 h48"
        stroke="var(--raw-ink)"
        stroke-width="2.5"
        stroke-linecap="round"
        stroke-linejoin="round"
      />
    </svg>
    <Transition name="fade" mode="out-in">
      <h3 :key="currentIndex">{{ currentMessage }}</h3>
    </Transition>
  </div>
</template>

<style scoped>
.loading-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-5);
  padding: var(--space-9) var(--space-5);
  text-align: center;
  height: 80vh;
  justify-content: center;
}

.briefcase {
  width: 80px;
  height: 80px;
}

.briefcase path {
  stroke-dasharray: 1;
  stroke-dashoffset: 1;
  animation: draw 3s ease-in-out infinite;
}

@keyframes draw {
  0% {
    stroke-dashoffset: 1;
  }
  50% {
    stroke-dashoffset: 0;
  }
  100% {
    stroke-dashoffset: -1;
  }
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 1.2s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
