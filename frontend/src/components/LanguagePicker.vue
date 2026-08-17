<script setup lang="ts">
const props = defineProps<{
  modelValue: string[]
  options: string[]
}>()
const emit = defineEmits<{
  'update:modelValue': [value: string[]]
}>()

function addLanguage(event: Event) {
  const select = event.target as HTMLSelectElement
  const lang = select.value
  if (!lang || props.modelValue.includes(lang)) {
    return
  }
  emit('update:modelValue', [...props.modelValue, lang])
  select.value = ''
}

function removeLanguage(lang: string) {
  emit(
    'update:modelValue',
    props.modelValue.filter((l) => l !== lang),
  )
}
</script>

<template>
  <div class="language-picker">
    <div class="language-tags" v-if="modelValue.length">
      <span v-for="lang in modelValue" :key="lang" class="language-tag">
        {{ lang }}
        <button type="button" @click="removeLanguage(lang)" :aria-label="`Remove ${lang}`">
          ×
        </button>
      </span>
    </div>

    <select @change="addLanguage">
      <option value="" disabled selected>Add a language...</option>
      <option
        v-for="lang in options"
        :key="lang"
        :value="lang"
        :disabled="modelValue.includes(lang)"
      >
        {{ lang }}
      </option>
    </select>
  </div>
</template>

<style scoped>
.language-picker {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

.language-tags {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
  padding: var(--space-1);
}

.language-tag {
  display: inline-flex;
  align-items: center;
  gap: var(--space-1);
  font-size: var(--text-sm);
  font-family: var(--font-mono);
  color: var(--color-accent);
  background: var(--color-accent-soft);
  border-radius: var(--radius-pill);
  padding: 2px var(--space-3);
}

.language-tag button {
  background: none;
  border: none;
  color: inherit;
  cursor: pointer;
  font-size: var(--text-base);
  line-height: 1;
  padding: 0;
}
</style>
