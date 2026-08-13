<template>
  <footer class="site-footer-outer">
    <div class="site-footer-inner">
      <span class="footer-version">v0.1.0</span>
      <nav class="footer-links">
        <RouterLink to="/imprint">Imprint</RouterLink>
        <RouterLink to="/privacy">Privacy</RouterLink>
        <RouterLink to="/terms">Terms</RouterLink>
      </nav>
    </div>
  </footer>
</template>

<style scoped>
.site-footer-outer {
  border-top: 1px dotted var(--color-border);
}

.site-footer-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1000px;
  margin: 0 auto;
  padding: var(--space-2) var(--space-6);
}

.footer-version {
  font-family: var(--font-mono);
  font-size: var(--text-sm);
  color: var(--color-text-muted);
}

.footer-links {
  display: flex;
  gap: var(--space-5);
}

.footer-links a {
  font-size: var(--text-sm);
  color: var(--color-text-muted);
}

.footer-links a:hover {
  color: var(--color-text);
}
</style>