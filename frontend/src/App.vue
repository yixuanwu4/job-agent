<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import { ref, onMounted, onUnmounted } from 'vue'

const glowRef = ref<HTMLElement | null>(null)

let targetX = 0
let targetY = 0
let currentX = 0
let currentY = 0
let rafId: number | null = null

function animate() {
  currentX += (targetX - currentX) * 0.15
  currentY += (targetY - currentY) * 0.15
  if (glowRef.value) {
    glowRef.value.style.transform = `translate(${currentX}px, ${currentY}px)`
  }
  rafId = requestAnimationFrame(animate)
}

function handleMouseMove(e: MouseEvent) {
  targetX = e.clientX
  targetY = e.clientY
}

onMounted(() => {
  window.addEventListener('mousemove', handleMouseMove)
  rafId = requestAnimationFrame(animate)
})

onUnmounted(() => {
  window.removeEventListener('mousemove', handleMouseMove)
  if (rafId !== null) cancelAnimationFrame(rafId)
})
</script>

<template>
  <header>
    <RouterLink to="/" class="logo-link" aria-label="Back to homepage">
      <img alt="Job Agent logo" class="logo" src="@/assets/job.png" />
    </RouterLink>
  </header>

  <main>
    <Teleport to="body">
      <div ref="glowRef" class="siri-glow" aria-hidden="true"></div>
    </Teleport>

    <RouterView />
  </main>
</template>

<style scoped>
header {
  position: sticky;
  padding-inline: 2rem;
  display: flex;
  align-items: center;
}

.logo-link {
  position: relative;
  height: 4rem;
  width: 4rem;
  margin: 2.5rem;
}

.logo {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  position: absolute;
}

.siri-glow {
  position: fixed;
  top: 0;
  left: 0;
  width: 1000px;
  height: 1000px;
  margin-left: -250px;
  margin-top: -250px;
  border-radius: 50%;
  pointer-events: none;
  opacity: 0.5;
  filter: blur(100px);
  z-index: 1;
  background: conic-gradient(from 180deg, #ff2ec4, #7b2ff7, #0091ff, #01a780, #c1a502, #ff2ec4);
  mask-image: radial-gradient(circle, black 0%, black 40%, transparent 75%);
  -webkit-mask-image: radial-gradient(circle, black 0%, black 40%, transparent 75%);
  mix-blend-mode: overlay;
  will-change: transform;
}

@media (max-width: 640px) {
  .logo-link {
    margin-inline-start: 0;
  }
}
</style>
