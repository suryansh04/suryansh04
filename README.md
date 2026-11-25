<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <img alt="Suryansh Pratap Singh. CS at Manipal University Jaipur, class of 2027. Full-stack and AI products, shipped to real users." src="assets/header-light.svg" width="100%">
</picture>

<p align="center">
  <a href="https://math.lerno.dev/"><b>Try Lerno</b></a> ·
  <a href="https://www.loom.com/share/43a95f1915294d149420c87aafa09799"><b>Watch the demo</b></a> ·
  <a href="#vote-on-the-next-lerno-lesson"><b>Vote on a lesson</b></a> ·
  <a href="https://x.com/suryanshhhhh_p"><b>X</b></a>
</p>

## Now building: Lerno

Ask a maths question and watch it turn into a short animated lesson. Three scenes drawn in Manim, narration under the film, a quick check after every scene, and a tutor that knows exactly where you paused.

<a href="https://math.lerno.dev/">
  <img alt="Lerno: opening a lesson from the dashboard, the scene animates while its narration highlights sentence by sentence" src="https://raw.githubusercontent.com/suryansh04/Lerno.ai/main/.github/assets/hero.webp" width="100%">
</a>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/stats-dark.svg">
  <img alt="50+ merged PRs at Better. 1st at CodeClash 2.0 among 1,000+ teams. Won Smart India Hackathon 2025." src="assets/stats-light.svg" width="100%">
</picture>

<details>
<summary><b>How a lesson gets made</b></summary>
<br>

1. **Plan.** Claude Sonnet turns the question into three scenes: narration, an animation brief and a quiz for each.
2. **Write and render.** All three scenes run in parallel. Claude writes the Manim code, and each scene renders in its own Modal sandbox. A failed render goes back to Claude for a fix, up to two times.
3. **Store.** Videos go to Supabase Storage. Lessons, scenes and notes live in Postgres. The player gets short-lived signed links.
4. **Watch.** The React app polls until the lesson is ready. The tutor runs on Claude Haiku with the scene and the paused moment as context.

**Stack:** React 19 · Vite · Tailwind 4 · FastAPI · Modal · Supabase · Claude · Manim  
[Source](https://github.com/suryansh04/Lerno.ai)

</details>

## Other things I've shipped

<p>
  <a href="https://github.com/suryansh04/WaveWatch"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-wavewatch-dark.svg"><img alt="WaveWatch: coastal hazard reporting for analysts and citizens. Won SIH 2025." src="assets/card-wavewatch-light.svg" width="49%"></picture></a>
  <a href="https://github.com/suryansh04/InternSetu"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-internsetu-dark.svg"><img alt="InternSetu: resume in, internships ranked by fit, then a mock interview. Runner-up IIC 2.0." src="assets/card-internsetu-light.svg" width="49%"></picture></a>
  <a href="https://github.com/suryansh04/sunskip"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-sunskip-dark.svg"><img alt="SunSkip: routes ranked by minutes spent in direct sun." src="assets/card-sunskip-light.svg" width="49%"></picture></a>
  <a href="https://github.com/suryansh04/GradeX"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/card-gradex-dark.svg"><img alt="GradeX: exams graded against a model answer, with feedback." src="assets/card-gradex-light.svg" width="49%"></picture></a>
</p>

## Where I've worked

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/timeline-dark.svg">
  <img alt="Journey: won SIH 2025; backend intern at BillCut Apr 2026; SDE intern at Better Jun 2026; building Lerno now; graduating 2027." src="assets/timeline-light.svg" width="100%">
</picture>

<details>
<summary><b>Better (Jalan Technologies) · SDE intern · Jun to Sep 2026</b></summary>
<br>

Worked on **Operate**, a self-hosted AI agent that finds the root cause of engineering incidents. 50+ merged PRs.

- Built the GitHub App auth flow: RS256-signed app JWTs swapped for 1-hour read-only installation tokens, HMAC-signed OAuth state, hashed install secrets checked in constant time, admin-only connect routes.
- Fixed GCP Cloud Logging, which was failing for every user.
- Shipped Dynatrace and SolarWinds integrations with alert webhooks, and a Sentry integration that opens cases on its own. Jenkins build history now links incidents to deploys.
- Owned the integrations UI in React and TypeScript.

</details>

<details>
<summary><b>BillCut · Backend intern · Apr 2026, 2 months</b></summary>
<br>

Built the Node.js and Express backend for **BillGPT**, BillCut's AI assistant for commerce and credit card rewards.

</details>

## Vote on the next Lerno lesson

Pick a topic. Your click opens a pre-filled issue. Hit **Submit**, and a GitHub Action counts the vote, redraws this chart and replies to you.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/votes-dark.svg">
  <img alt="Live vote count for the next Lerno lesson" src="assets/votes-light.svg" width="100%">
</picture>

<p align="center">
  <a href="https://github.com/suryansh04/suryansh04/issues/new?title=vote%3A%20fourier%20series&body=Just%20hit%20Submit.%20Your%20vote%20is%20counted%20in%20about%20a%20minute."><b>fourier series</b></a> ·
  <a href="https://github.com/suryansh04/suryansh04/issues/new?title=vote%3A%20eigenvectors&body=Just%20hit%20Submit.%20Your%20vote%20is%20counted%20in%20about%20a%20minute."><b>eigenvectors</b></a> ·
  <a href="https://github.com/suryansh04/suryansh04/issues/new?title=vote%3A%20bayes%20theorem&body=Just%20hit%20Submit.%20Your%20vote%20is%20counted%20in%20about%20a%20minute."><b>bayes theorem</b></a> ·
  <a href="https://github.com/suryansh04/suryansh04/issues/new?title=vote%3A%20taylor%20series&body=Just%20hit%20Submit.%20Your%20vote%20is%20counted%20in%20about%20a%20minute."><b>taylor series</b></a> ·
  <a href="https://github.com/suryansh04/suryansh04/issues/new?title=vote%3A%20central%20limit%20theorem&body=Just%20hit%20Submit.%20Your%20vote%20is%20counted%20in%20about%20a%20minute."><b>central limit theorem</b></a>
</p>

## What I build with

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/stack-dark.svg">
  <img alt="Stack: TypeScript, Python, Java, C++; React, Next.js, Tailwind; FastAPI, Node.js, Express; PostgreSQL, MongoDB, Supabase, Firebase; Claude API, Manim, RAG; Docker, AWS, Vercel, Modal; Flutter, SwiftUI." src="assets/stack-light.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/suryansh04/suryansh04/output/snake-dark.svg">
  <img alt="A snake eating my contribution graph, redrawn every day" src="https://raw.githubusercontent.com/suryansh04/suryansh04/output/snake-light.svg" width="100%">
</picture>

<p align="center"><sub>A maths topic that never clicked for you? <a href="https://math.lerno.dev/">Ask Lerno</a> and watch it explained.</sub></p>
