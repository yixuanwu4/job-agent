<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>

<template>
  <main class="home">
    <div class="grid-frame">
      <section class="hero">
        <h1>Invest your time on the most matched jobs</h1>
        <p class="hero-sub">
          Upload your CV, add what you're looking for, and see how you match — right now, or every
          morning by subscribing.
        </p>
        <RouterLink to="/tool" class="cta">Try it now — no signup, nothing saved</RouterLink>
      </section>
      <section class="paths">
        <RouterLink to="/tool" class="path-card path-card--try">
          <h2>Try it once</h2>
          <p>
            Upload your CV, get your matches, done. Nothing is saved unless you choose to subscribe
            below.
          </p>
          <div class="card-image-placeholder">
            <span>Screenshot: instant report email</span>
          </div>
        </RouterLink>

        <RouterLink to="/tool?mode=subscribe" class="path-card path-card--subscribe">
          <h2>Subscribe and get daily matches</h2>
          <p>
            A short email each morning with new postings that fit — plus a link to update your
            search or stop anytime.
          </p>
          <div class="card-image-placeholder">
            <span>Screenshot: daily digest email</span>
          </div>
        </RouterLink>
      </section>
    </div>
  </main>
</template>

<style scoped>
.home {
  max-width: 1000px;
  margin: 0 auto;
  padding: var(--space-9) var(--space-4) var(--space-8);
}

.hero {
  text-align: center;
  margin-inline: var(--space-9);
  margin-bottom: var(--space-8);
}

.hero h1 {
  font-size: var(--text-hero);
}

.hero-sub {
  font-size: var(--text-lg);
  color: var(--color-text-muted);
  max-width: 600px;
  margin: 0 auto var(--space-6);
}

.cta {
  display: inline-block;
  background: var(--color-accent);
  color: var(--raw-paper);
  padding: var(--space-3) var(--space-5);
  border-radius: var(--radius-control);
  font-weight: 600;
  text-decoration: none;
}

.cta:hover {
  text-decoration: none;
  opacity: 0.9;
}

.proof {
  margin-bottom: var(--space-8);
}

.screenshot-placeholder {
  aspect-ratio: 16 / 10;
  border: 1px dashed var(--color-border-hover);
  border-radius: var(--radius-card);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--color-text-muted);
  font-size: var(--text-sm);
  background: var(--color-surface);
}

.paths {
  display: grid;
  grid-template-columns: 1fr 1fr;
  margin-bottom: var(--space-8);
  min-height: 30rem;
  border: 2px solid var(--color-border);
  border-radius: var(--radius-card);
  overflow: hidden;
}

.path-card {
  display: flex;
  flex-direction: column;
  background: var(--color-surface);
  padding: var(--space-5);
  gap: var(--space-6);
}

.path-card h2 {
  font-size: var(--text-lg);
  margin-bottom: var(--space-3);
}

.path-card p {
  color: var(--color-text-muted);
}

.path-card--try {
  border-right: 2px solid var(--color-border);
}

.path-card--subscribe {
  background-color: var(--raw-grey);
  overflow: hidden;
}

@media (max-width: 640px) {
  .hero {
    margin-inline: 0;
  }
  .paths {
    grid-template-columns: 1fr;
  }
  .path-card--try {
    border-right: none;
    border-bottom: 2px solid var(--color-border);
  }
}
</style>
