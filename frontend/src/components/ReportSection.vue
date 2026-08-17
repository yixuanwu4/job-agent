<script setup lang="ts">
import { computed } from 'vue'
import showdown from 'showdown'

const props = defineProps<{
  title: string
  content: string
}>()

const converter = new showdown.Converter({ sanitize: true })
const htmlContent = computed(() => converter.makeHtml(props.content))
</script>

<template>
  <section class="report-section">
    <h2>{{ title }}</h2>
    <div class="markdown-content" v-html="htmlContent"></div>
  </section>
</template>

<style scoped>
.report-section {
  padding: var(--space-6) 0;
  border-bottom: 1px dashed var(--color-border);
}

.report-section h2 {
  font-size: var(--text-lg);
  margin-bottom: var(--space-4);
}

.markdown-content :deep(h1),
.markdown-content :deep(h2),
.markdown-content :deep(h3) {
  font-weight: 600;
  margin-top: var(--space-5);
  margin-bottom: var(--space-2);
}

.markdown-content :deep(h1) {
  font-size: var(--text-lg);
  font-weight: 700;
}
.markdown-content :deep(h2) {
  font-size: var(--text-base);
  font-weight: 700;
}
.markdown-content :deep(h3) {
  font-size: var(--text-base);
  font-weight: 600;
}

.markdown-content :deep(p) {
  color: var(--color-text);
  line-height: 1.6;
}

.markdown-content :deep(ul),
.markdown-content :deep(ol) {
  margin-bottom: var(--space-3);
  padding-left: var(--space-5);
}

.markdown-content :deep(li) {
  margin-bottom: var(--space-2);
  line-height: 1.6;
}

.markdown-content :deep(strong) {
  font-weight: 600;
  color: var(--color-heading);
}
</style>
