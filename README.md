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
> 📧 [Reach out to discuss your project](mailto:your-email@example.com) or DM me on [LinkedIn](your-linkedin-url).

---

## 🛠️ Tech Stack & Systems Arsenal

```
Languages  │ TypeScript • JavaScript • Python • PHP • SQL • C++
Frontend   │ React (Vite/Next.js) • Vue 3 • React Native (Expo) • HTML5 • CSS3 • Tailwind CSS
Backend    │ Node.js • Bun Runtime • Laravel 10 • Supabase (Postgres)
Databases  │ PostgreSQL (RLS isolation) • SQLite (WAL journaling, FTS5)
DevOps     │ Docker • GitHub Actions CI/CD • Linux System Administration • Git
```

---

## 🚀 Featured Engineering Systems

These aren't boilerplate templates. Below are production-grade systems built to solve complex architectural challenges:

### 🪐 [LogiFlow Hub](https://github.com/Hubrisdog/logiflow-hub)
*Enterprise-grade inventory intelligence and logistics orchestration engine.*
- **Tech Stack**: React 18, TypeScript, React Native (Expo), Supabase, PostgreSQL.
- **The Hard Problems Solved**:
  - Engineered a **GAAP-compliant FIFO Accounting Ledger** that prevents valuation drift across split-batch consume operations, computing dynamic Cost of Goods Sold (COGS).
  - Built an **Offline-Resilient Sync Queue** with a custom `isReconciling` mutex lock to prevent network reconnect storms from executing out-of-order writes.
  - Secured multi-tenancy at the database layer using strict **PostgreSQL Row Level Security (RLS)** rather than relying on vulnerable client-side scoping.

### 🛡️ [Aegis Threat Intel](https://github.com/Hubrisdog/aegis-threat-intel)
*Self-hosted, air-gapped Threat Intelligence Platform (TIP) with cognitive AI analysis.*
- **Tech Stack**: Vue 3, Bun Runtime, SQLite (WAL / FTS5), Python, Anthropic / Ollama.
- **The Hard Problems Solved**:
  - Tuned **SQLite WAL journaling** and busy timeouts (`busy_timeout = 5000`) to guarantee background threat ingestion routines never lock or block real-time analyst searches.
  - Implemented an **FTS5 Search Fallback** mechanism that handles special character syntax failures (like dots in IP addresses) by gracefully falling back to wildcard `LIKE` indexing.
  - Created a custom **automated defanging parser** for secure threat reporting, transforming live indicators (`evil.com` ➡️ `evil[.]com`) before data exports.

### 📅 [Nexa](https://github.com/Hubrisdog/nexa)
*Multi-tenant scheduling and sales CRM platform.*
- **Tech Stack**: Laravel 10, Vue 3 SPA, Vite, Google Calendar OAuth.
- **The Hard Problems Solved**:
  - Designed a **Workload-Balanced Round-Robin Algorithm** that calculates active provider loads and routes booking leads to the least-busy staff member.
  - Built a secure **Outbound Webhook Pipeline** using **HMAC SHA256 header signatures** to authenticate event payloads dispatched to external developer targets.
  - Developed a dynamic **Domain & SSL Wizard** allowing custom branding isolation, custom CSS injection (`--primary-color`), and simulated Let's Encrypt DNS checks.

---

## 🎯 Current Operational Focus

- **Blending Systems Theory & Production Implementation**: Currently completing a BS in Information Technology while building and maintaining production SaaS architectures.
- **Continuous Shipping**: Implementing localized Retrieval-Augmented Generation (RAG) for security telemetry, optimized DB indexing, and zero-trust multi-tenant systems.

> *Turning complex operational friction into clean, reliable, and auditable software.*
