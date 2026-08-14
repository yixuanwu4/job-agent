<template>
  <div class="legal-page">
    <h1>Imprint</h1>
    <p>The identity of the owner of this application is stated below.</p>
    <div id="general">
      <p><strong>Yixuan Wu</strong></p>
      <p>c/o openscript GmbH</p>
      <p>Europa-Strasse 30</p>
      <p>8152 Glattbrugg</p>
      <p><a href="mailto:job-agent@yixuan.ch">job-agent@yixuan.ch</a></p>
    </div>

    <div id="profile">
      <h2>The profile</h2>
      <p>This project is presented on the following platform:</p>
      <ul>
        <li>
          <a href="https://github.com/yixuanwu4/job-agent"> GitHub </a>
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
.legal-page {
  max-width: 640px;
  margin: 0 auto;
  padding: var(--space-8) var(--space-5);
}

p {
  line-height: 1.6;
  color: var(--color-text-muted);
}

a {
  text-decoration: underline;
}

li {
  line-height: 1.6;
}

#general {
  margin-block-start: var(--space-4);
}

#profile {
  margin-top: var(--space-8);
}
</style>
