<p align="center">
  <img src="banner.png" alt="Hubris GitHub Profile Banner" width="100%">
</p>

# Hey, I'm Phillippe (Hubris) 👋

**Systems Engineer & Architect specializing in offline-resilient SaaS engines, air-gapped threat intelligence platforms, and automated workflow orchestrations.**

I design and build software that replaces manual friction with high-performance, automated business systems. My work focuses on database concurrency, multi-tenant security, and robust offline-first synchronization.

> [!NOTE]
> ### ⚡ Available for Freelance & Collaboration
> I am currently open to select freelance projects, architectural consulting, and contract engagements.  
> **Have a complex workflow that needs automating, a database bottleneck to solve, or a SaaS platform to build?**  
> 📧 [Reach out to discuss your project: alphllppegarado@gmail.com](mailto:alphllppegarado@gmail.com)

---

## 🚀 Featured Engineering

<table border="0">
  <tr>
    <td width="33.3%" valign="top">
      <h4>🛡️ <a href="https://github.com/Hubrisdog/aegis-threat-intel">aegis-threat-intel</a></h4>
      <p>Self-hosted, privacy-first threat intelligence platform (TIP) for local IOC correlation and AI analysis.</p>
      <img src="https://img.shields.io/badge/Security-Threat_Intel-red?style=flat-square" alt="Security badge">
      <img src="https://img.shields.io/badge/AI-Analysis-purple?style=flat-square" alt="AI badge">
    </td>
    <td width="33.3%" valign="top">
      <h4>📦 <a href="https://github.com/Hubrisdog/logiflow-hub">logiflow-hub</a></h4>
      <p>Premium enterprise-grade inventory intelligence and logistics orchestration platform built with React, TypeScript, and Supabase.</p>
      <img src="https://img.shields.io/badge/Stack-React_%7C_Supabase-blue?style=flat-square" alt="Stack badge">
      <img src="https://img.shields.io/badge/Enterprise-SaaS-green?style=flat-square" alt="SaaS badge">
    </td>
    <td width="33.3%" valign="top">
      <h4>📅 <a href="https://github.com/Hubrisdog/nexa">nexa</a></h4>
      <p>Multi-tenant scheduling and CRM platform with round-robin lead allocation and OAuth sync.</p>
      <img src="https://img.shields.io/badge/Backend-Laravel_10-red?style=flat-square" alt="Backend badge">
      <img src="https://img.shields.io/badge/Frontend-Vue_3-green?style=flat-square" alt="Frontend badge">
    </td>
  </tr>
</table>

---

## 🧠 Deep-Dive Architecture & Core Challenges

These represent the specific engineering challenges solved within the featured systems:

### 🪐 LogiFlow Hub
- Engineered a **GAAP-compliant FIFO Accounting Ledger** that prevents valuation drift across split-batch consume operations, computing dynamic Cost of Goods Sold (COGS).
- Built an **Offline-Resilient Sync Queue** with a custom `isReconciling` mutex lock to prevent network reconnect storms from executing out-of-order writes.
- Secured multi-tenancy at the database layer using strict **PostgreSQL Row Level Security (RLS)** rather than relying on vulnerable client-side scoping.

### 🛡️ Aegis Threat Intel
- Tuned **SQLite WAL journaling** and busy timeouts (`busy_timeout = 5000`) to guarantee background threat ingestion routines never lock or block real-time analyst searches.
- Implemented an **FTS5 Search Fallback** mechanism that handles special character syntax failures (like dots in IP addresses) by gracefully falling back to wildcard `LIKE` indexing.
- Created a custom **automated defanging parser** for secure threat reporting, transforming live indicators (`evil.com` ➡️ `evil[.]com`) before data exports.

### 📅 Nexa
- Designed a **Workload-Balanced Round-Robin Algorithm** that calculates active provider loads and routes booking leads to the least-busy staff member.
- Built a secure **Outbound Webhook Pipeline** using **HMAC SHA256 header signatures** to authenticate event payloads dispatched to external developer targets.
- Developed a dynamic **Domain & SSL Wizard** allowing custom branding isolation, custom CSS injection (`--primary-color`), and simulated Let's Encrypt DNS checks.

---

## 🛠️ Tech Stack & Arsenal

| Category | Tools & Technologies |
| :--- | :--- |
| **Languages** | ![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![PHP](https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white) ![C++](https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white) |
| **Frontend** | ![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB) ![Vue.js](https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D) ![Next.js](https://img.shields.io/badge/Next.js-black?style=for-the-badge&logo=next.js&logoColor=white) ![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white) ![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white) ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) |
| **Backend & DB** | ![Node.js](https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white) ![Bun](https://img.shields.io/badge/Bun-000000?style=for-the-badge&logo=bun&logoColor=white) ![Laravel](https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white) ![Supabase](https://img.shields.io/badge/Supabase-1C1C1E?style=for-the-badge&logo=supabase&logoColor=3ECF8E) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white) ![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white) |
| **Security & DevOps** | ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white) |

---

## 🎯 Current Operational Focus

- **Blending Systems Theory & Production Implementation**: Currently completing a BS in Information Technology while building and maintaining production SaaS architectures.
- **Continuous Shipping**: Implementing localized Retrieval-Augmented Generation (RAG) for security telemetry, optimized DB indexing, and zero-trust multi-tenant systems.

<p align="center">
  <i>“Building tomorrow's secure systems, one repository at a time.”</i>
</p>
