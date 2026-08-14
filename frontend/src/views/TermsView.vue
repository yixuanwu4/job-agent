<template>
  <div class="legal-page">
    <h1>Terms</h1>
    <p class="legal-version">Version 1.0</p>

    <h2>About This Service</h2>
    <p>
      Job Agent is a personal, free project, provided as-is and without warranty. It's currently in
      active development.
    </p>

    <h2>No Guarantee of Outcome</h2>
    <p>
      Job matches, scores, and advice are generated automatically using third-party job listings and
      AI analysis. They may be inaccurate, incomplete, or out of date. Nothing on this website
      guarantees any outcome in your job search, and it shouldn't be your only source when
      evaluating a job opportunity.
    </p>

    <h2>Third-Party Content</h2>
    <p>
      Job listings and links to external application pages come from third-party sources (currently
      Adzuna) and are outside our control. We're not responsible for the accuracy of listings, or
      for the content of any third-party site you're taken to.
    </p>

    <h2>Disclaimer of Liability</h2>
    <p>
      Any claims relating to damage caused by the use of, or inability to use, this service — or by
      relying on inaccurate or incomplete information it provides — are excluded to the extent
      permitted by law.
    </p>

    <h2>Changes to the Service</h2>
    <p>This project may be changed, limited, or discontinued at any time, without prior notice.</p>

    <h2>Reuse and Licensing</h2>
    <p>
      The source code for this project is licensed under CC BY-NC 4.0 — you're free to use and adapt
      it for non-commercial purposes, with attribution. See the LICENSE file in the repository for
      full terms. For commercial use, contact us at the address given in the Imprint.
    </p>
  </div>
</template>

<style scoped>
.legal-page {
  max-width: 640px;
  margin: 0 auto;
  padding: var(--space-8) var(--space-5);
}
.legal-page h2 {
  font-size: var(--text-lg);
  margin-top: var(--space-6);
  margin-bottom: var(--space-2);
}
.legal-page p {
  color: var(--color-text-muted);
  margin-bottom: var(--space-3);
  line-height: 1.6;
}
.legal-version {
  font-size: var(--text-sm);
  color: var(--color-text-muted);
  margin-top: calc(-1 * var(--space-2));
}
</style>
