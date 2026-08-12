<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>

<template>
  <div class="home">
    <div class="grid-frame">
      <section class="hero">
        <h1>Invest your time on the most matched jobs</h1>
        <p class="hero-sub">
          Upload your CV, add what you're looking for, and see how you match — right now, or every
          morning by subscribing.
        </p>
      </section>

      <section class="paths">
        <div class="path-card path-card--try">
          <div class="path-header">
            <span class="path-eyebrow">ONE-TIME</span>

            <RouterLink to="/tool" class="path-title-link">
              <h2>Try it once</h2>
            </RouterLink>

            <p class="path-description">
              See how well your CV matches today's open roles. Nothing is saved unless you choose to
              subscribe.
            </p>
          </div>

          <ul class="path-benefits">
            <li>
              <span class="feature-number">01</span>
              <div>
                <div class="feature-title">Match score</div>
                <p>See how well your CV fits each role.</p>
              </div>
            </li>

            <li>
              <span class="feature-number">02</span>
              <div>
                <div class="feature-title">CV gaps</div>
                <p>See what's missing from your CV.</p>
              </div>
            </li>

            <li>
              <span class="feature-number">03</span>
              <div>
                <div class="feature-title">Interview prep</div>
                <p>Get questions tailored to your gaps.</p>
              </div>
            </li>
          </ul>

          <RouterLink class="cta cta--glass" to="/tool">
            <button>Try it <span>→</span></button>
          </RouterLink>
        </div>

        <div class="path-card path-card--subscribe">
          <div class="path-header">
            <span class="path-eyebrow">DAILY</span>

            <RouterLink to="/tool?mode=subscribe" class="path-title-link">
              <h2>Get daily matches</h2>
            </RouterLink>

            <p class="path-description">
              Get a short email every morning with new postings that fit.
            </p>
          </div>

          <ul class="path-benefits">
            <li>
              <span class="feature-number">01</span>
              <div>
                <div class="feature-title">Fresh matches</div>
                <p>New postings from the last 24 hours.</p>
              </div>
            </li>

            <li>
              <span class="feature-number">02</span>
              <div>
                <div class="feature-title">Private link</div>
                <p>Update or cancel your subscription anytime.</p>
              </div>
            </li>

            <li>
              <span class="feature-number">03</span>
              <div>
                <div class="feature-title">No account</div>
                <p>Just your inbox — no password needed.</p>
              </div>
            </li>
          </ul>

          <RouterLink class="cta cta--glass" to="/tool?mode=subscribe">
            <button>Subscribe <span>→</span></button>
          </RouterLink>
        </div>
      </section>
    </div>
  </div>
</template>

<style scoped>
.home {
  max-width: 1000px;
  margin: 0 auto;
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

.paths {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-6);
  margin-bottom: var(--space-8);
}

.path-card {
  display: flex;
  flex-direction: column;
  padding: var(--space-6);
  border: 1px solid rgba(20, 20, 20, 0.16);
  border-radius: var(--radius-card);
  background: linear-gradient(145deg, rgba(255, 255, 255, 0.72), rgba(245, 247, 248, 0.52));
  box-shadow:
    0 1px 2px rgba(0, 0, 0, 0.03),
    0 12px 40px rgba(0, 0, 0, 0.04);
}

.path-card:hover {
  background: linear-gradient(145deg, rgba(255, 255, 255, 0.9), rgba(245, 247, 248, 0.7));
  border-color: var(--color-card-border);
}

.path-header {
  display: flex;
  flex-direction: column;
}

.path-eyebrow {
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--color-text-muted);
  margin-bottom: var(--space-3);
}

.path-title-link {
  color: inherit;
  text-decoration: none;
}

.path-card h2 {
  font-size: var(--text-xl);
  margin: 0 0 var(--space-3);
  letter-spacing: -0.02em;
}

.path-description {
  max-width: 32rem;
  margin: 0;
  color: var(--color-text-muted);
  line-height: 1.55;
}

.path-benefits {
  list-style: none;
  padding: 0;
  margin: var(--space-6) 0 0;
}

.path-benefits li {
  display: grid;
  grid-template-columns: 2rem 1fr;
  column-gap: var(--space-3);
  padding-block: var(--space-4);
  border-top: 1px solid rgba(20, 20, 20, 0.09);
}

.feature-number {
  font-size: 0.72rem;
  font-weight: 600;
  color: var(--color-text-muted);
  padding-top: 0.15rem;
  letter-spacing: 0.04em;
}

.feature-title {
  font-size: var(--text-md);
  font-weight: 600;
  margin-bottom: 0.2rem;
}

.path-benefits p {
  font-size: var(--text-sm);
  color: var(--color-text-muted);
  line-height: 1.45;
  margin: 0;
}

.cta {
  display: flex;
  justify-content: flex-end;
  margin-top: auto;
  padding-top: var(--space-5);
  text-decoration: none;
}

.cta--glass button {
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0.65rem 1rem;

  border: 1px solid rgba(255, 255, 255, 0.65);
  border-radius: 999px;

  background: rgba(255, 255, 255, 0.38);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);

  box-shadow:
    0 2px 8px rgba(0, 0, 0, 0.06),
    inset 0 1px 0 rgba(255, 255, 255, 0.8);

  font-size: var(--text-md);
  color: var(--color-text);
  cursor: pointer;

  transition:
    background-color 0.2s ease,
    transform 0.2s ease,
    box-shadow 0.2s ease;
}

.cta--glass button span {
  transition: transform 0.2s ease;
}

.cta--glass button:hover {
  background: rgba(255, 255, 255, 0.62);
  box-shadow:
    0 4px 14px rgba(0, 0, 0, 0.08),
    inset 0 1px 0 rgba(255, 255, 255, 0.9);
  transform: translateY(-1px);
}

.cta--glass button:hover span {
  transform: translateX(3px);
}

@media (max-width: 640px) {
  .hero {
    margin-inline: 0;
  }

  .paths {
    grid-template-columns: 1fr;
  }
}
</style>
