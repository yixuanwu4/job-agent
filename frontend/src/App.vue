<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <div class="logo">
      <a href="/">
        <img src="../src/assets/job.png" />
      </a>
    </div>
    <div class="wrapper">
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/tool">Tool</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
  padding-inline: 2rem;
}

.logo {
  display: block;
  width: 4rem;
  height: 4rem;
  margin: 2rem;
  overflow: hidden;
}

.logo img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  display: block;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 2px solid var(--color-border);
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
  }
}
</style>
