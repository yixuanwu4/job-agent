<script setup lang="ts">
import SearchForm from '@/components/SearchForm.vue';
</script>

<template>
  <div class="tool">
    <h1>This is the tool page</h1>
    <SearchForm />
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
