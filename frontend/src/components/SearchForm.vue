<script setup lang="ts">
import { ref } from 'vue'

const cv = ref<File | null>(null)
const role = ref("")
const location = ref("")
const country = ref("")
const preferred_language = ref("")
const email = ref("")

function get_cv(event: Event){
    const target = event.target as HTMLInputElement
    cv.value = target.files?.[0] ?? null
}
</script>

<template>
    <h1>Search Form</h1>
    <div class="container">
        <label>Upload your CV (PDF or TXT)
            <input type="file" id="file" @change="get_cv" accept=".pdf, .txt" />
        </label>
        <label>Desired job title 
            <input type="text" v-model="role" placeholder="e.g. Frontend Developer" />
        </label>
        <label>Location 
            <input type="text" v-model="location" placeholder="e.g. London" />
        </label>
        <label>Country 
            <input type="text" v-model="country" placeholder="e.g. United Kingdom" />
        </label>
        <label>Preferred job posting language 
            <input type="text" v-model="preferred_language" placeholder="e.g. English" />
        </label>
        <label>Email 
            <input type="email" v-model="email" />
        </label>
    </div>
</template>

<style>
.container {
    display: flex;
    flex-direction: column;
}
</style>