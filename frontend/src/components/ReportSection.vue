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
    <section>
        <h2>{{ title }}</h2>
        <div v-html="htmlContent"></div>
    </section>
</template>