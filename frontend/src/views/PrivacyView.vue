<template>
  <div class="legal-page">
    <h1>Privacy</h1>

    <h2>What's collected</h2>
    <p>
      If you generate a one-off report, your CV is read into memory to produce the report and then
      discarded - nothing is stored.
    </p>
    <p>
      If you subscribe, your email address, CV, and search preferences (job titles, location,
      country, preferred language) are stored so the daily job can run.
    </p>

    <h2>Who it's shared with</h2>
    <ul>
      <li>Anthropic: CV and job description content, to generate the report</li>
      <li>Adzuna: search keywords only, no personal data</li>
      <li>Supabase: stores subscriber data and CV files</li>
      <li>Resend: delivers emails</li>
    </ul>

    <h2>How long it's kept</h2>
    <p>
      Subscriber data is kept until you unsubscribe. Unsubscribing permanently deletes your database
      record and CV file — this is not reversible.
    </p>

    <h2>Your rights</h2>
    <p>
      To ask what's stored about you, or to have it removed outside of the unsubscribe flow, contact
      <a href="mailto:job-agent@yixuan.ch">job-agent@yixuan.ch</a>.
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
.legal-page p,
.legal-page li {
  color: var(--color-text-muted);
  margin-bottom: var(--space-2);
  line-height: 1.6;
}
.legal-page ul {
  padding-left: var(--space-5);
}
</style>
