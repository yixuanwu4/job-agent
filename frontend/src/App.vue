<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <RouterLink to="/" class="logo-link" aria-label="Back to homepage">
      <img alt="Job Agent logo" class="logo" src="@/assets/job.png" />
    </RouterLink>
  </header>

  <main>
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
</style>
