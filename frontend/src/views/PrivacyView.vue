<template>
  <div class="legal-page">
    <h1>Privacy Policy</h1>
    <p class="legal-version">Version 1.0</p>

    <h2>General Information</h2>
    <p>
      Based on Article 13 of the Swiss Federal Constitution and the Swiss Federal Act on Data
      Protection (FADP), everyone has the right to protection of their privacy and protection
      against misuse of their personal data. This project takes the protection of your data
      seriously and processes it confidentially, in accordance with applicable data protection law
      and this policy.
    </p>
    <p>
      We make reasonable efforts, together with our hosting and infrastructure providers, to protect
      data against unauthorized access, loss, misuse, or falsification. Data transmission over the
      internet can have security vulnerabilities, and complete protection against third-party access
      cannot be guaranteed.
    </p>
    <p>
      By using this website, you consent to the collection, processing, and use of data as described
      below.
    </p>

    <h2>Contact Details of the Responsible Party</h2>
    <p><strong>Person:</strong> Yixuan Wu</p>
    <p>
      <strong>Address:</strong> c/o openscript GmbH, Europa-Strasse 30, 8152 Glattbrugg, Switzerland
    </p>
    <p><strong>Email:</strong> <a href="mailto:job-agent@yixuan.ch">job-agent@yixuan.ch</a></p>

    <h2>What's Collected</h2>
    <p>
      <strong>Generating a one-off report</strong> — your CV is read into memory to produce the
      report and then discarded immediately afterward. Nothing is written to a database or file
      storage.
    </p>
    <p>
      <strong>Subscribing</strong> — your email address, CV, and search preferences (job titles,
      location, country, preferred posting language) are stored so the daily matching job has
      something to run against.
    </p>

    <h2>Who It's Shared With</h2>
    <p>
      Job Agent runs on third-party infrastructure. The following providers process data as part of
      delivering the service:
    </p>
    <ul>
      <li>
        <strong>Anthropic</strong> — receives your CV and job description content to generate match
        scores and advice
      </li>
      <li>
        <strong>Adzuna</strong> — receives search keywords only (job titles, location); no personal
        data
      </li>
      <li>
        <strong>Supabase</strong> — stores subscriber email addresses, CV files, and search
        preferences
      </li>
      <li><strong>Resend</strong> — delivers emails on our behalf</li>
      <li>
        <strong>Render / GitHub Pages</strong> — host the backend and frontend. Standard server log
        data (IP address, request time, browser info) may be recorded by these providers as part of
        normal hosting operation. We don't have direct access to these logs and don't use them for
        tracking.
      </li>
    </ul>

    <h2>Cookies</h2>
    <p>This website does not use cookies.</p>

    <h2>Retention &amp; Deletion</h2>
    <p>
      Subscriber data is kept for as long as the subscription is active. Unsubscribing permanently
      deletes your database record and stored CV file — this cannot be undone, and there's nothing
      left afterward to request removal of.
    </p>

    <h2>Your Rights</h2>
    <p>
      If you're subscribed, every email includes a unique link to view or update the information
      stored about you. You can unsubscribe — and permanently delete your data — at any time through
      that same link, without needing to contact anyone.
    </p>
    <p>
      To ask what's stored about you outside of that flow, or if you have any other question about
      this policy, contact us at the address above.
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
  margin-bottom: var(--space-3);
  line-height: 1.6;
}
.legal-page ul {
  padding-left: var(--space-5);
}
.legal-version {
  font-size: var(--text-sm);
  color: var(--color-text-muted);
  margin-top: calc(-1 * var(--space-2));
}
</style>
