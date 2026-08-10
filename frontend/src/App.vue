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
  padding-inline: 2rem;
  display: flex;
  align-items: center;
}

.logo-link {
  height: 4rem;
  width: 4rem;
  margin: 2rem;
}


@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }
}
</style>
