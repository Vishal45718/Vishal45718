<!--
  Vishal Varukolu — GitHub Profile README
  Live profile snapshot: assets/profile-dashboard.svg
  Generator: scripts/generate_profile_dashboard.py
  Schedule: .github/workflows/profile-dashboard.yml
-->

<div align="center">

# Vishal Varukolu

**CSE @ IIT Hyderabad · Class of 2027**

`systems` · `backend infrastructure` · `compilers` · `applied ML`

<br/>

<a href="mailto:vv14022006@gmail.com">
  <img src="https://img.shields.io/badge/EMAIL-contact-172033?style=flat-square&logo=gmail&logoColor=67E8A5" alt="Email"/>
</a>
<a href="https://linkedin.com/in/Vishal-V-ab8a2131b/">
  <img src="https://img.shields.io/badge/LINKEDIN-connect-172033?style=flat-square&logo=linkedin&logoColor=67E8A5" alt="LinkedIn"/>
</a>
<a href="https://github.com/Vishal45718">
  <img src="https://img.shields.io/badge/GITHUB-Vishal45718-172033?style=flat-square&logo=github&logoColor=67E8A5" alt="GitHub"/>
</a>

<br/><br/>

<a href="https://github.com/Vishal45718">
  <img src="./assets/profile-dashboard.svg" width="100%" alt="Terminal-style live GitHub dashboard showing public repositories, stars, forks, and followers"/>
</a>

<sub><code>./profile --snapshot</code> · public GitHub metrics · daily refresh</sub>

</div>

---

## `01 / whoami`

I like working close to the metal and tracing problems across the stack — from compiler passes and data structures to distributed services and GPU training systems.

| | |
|:--|:--|
| **Interests** | Systems, backend infrastructure, compilers, applied ML |
| **Currently building** | Tools for reasoning about failures in distributed training |
| **Engineering philosophy** | Small, testable components; explicit trade-offs; measurements over claims of scale without benchmarks |

---

## `02 / selected-work`

### `[01] TrainPulse`
**Research · Distributed training observability**

Co-developed a lightweight fault-localization pipeline for multi-node LLM training. It combines iteration-time change detection, component-level anomaly scores, and dependency-aware reasoning to narrow down likely sources of fail-slow behavior.

**Reported evaluation**

- **100% single-fault localization accuracy**
- **Under 1% runtime overhead**, compared with **2.18% overhead for the PyTorch profiler**
- Evaluated on a **4-node cluster** fine-tuning **Llama 3 8B**

**Stack:** `Python` · `PyTorch DDP` · Distributed GPU training

> Under submission to ACM SIGMETRICS 2027. The research code is not public yet; contact me for details.

---

### `[02] LAOP Compiler` · [Repository ↗](https://github.com/Vishal45718/LAOP-compiler)
**Compiler backend · C++**

A domain-specific compiler for linear-algebra expressions. The backend performs semantic checks and emits Eigen-based C++ code, with matrix-chain ordering as an optimization pass.

**Stack:** `C++` · `Eigen`

---

### `[03] Self-Healing RAG` · [Repository ↗](https://github.com/Vishal45718/Self_Healing_RAG)
**Retrieval and evaluation · Python**

A RAG pipeline that can critique its own response path: reformulate a query, retry grounded generation, or abstain when the evidence is weak. Includes an evaluation harness for comparison against baseline retrieval.

**Stack:** `Python` · `LangGraph` · `ChromaDB` · `Sentence Transformers`

---

### `[04] Scalable Recommendation System` · [Repository ↗](https://github.com/Vishal45718/Scalable_Recommendation_System)
**Backend / data infrastructure · Python**

An event-driven recommendation-system project exploring Kafka ingestion, vector retrieval with FAISS, and a Redis-backed feature cache.

**Stack:** `FastAPI` · `Kafka` · `FAISS` · `Redis` · `PostgreSQL`

---

### `[05] Inventory Management System` · [Repository ↗](https://github.com/Vishal45718/IMS_Full-Stack-Inventory-Management-System)
**Full-stack · Go + web**

A multi-branch inventory application with REST APIs, JWT authentication, role-based access, and relational data constraints around stock and orders.

**Stack:** `Go` · `Gin` · `MySQL` · `Next.js`

---

## `03 / toolchain`

<div align="center">

![C++](https://img.shields.io/badge/C++-172033?style=flat-square&logo=cplusplus&logoColor=67E8A5)
![Python](https://img.shields.io/badge/Python-172033?style=flat-square&logo=python&logoColor=67E8A5)
![Go](https://img.shields.io/badge/Go-172033?style=flat-square&logo=go&logoColor=67E8A5)
![TypeScript](https://img.shields.io/badge/TypeScript-172033?style=flat-square&logo=typescript&logoColor=67E8A5)
![SQL](https://img.shields.io/badge/SQL-172033?style=flat-square&logo=mysql&logoColor=67E8A5)
![Linux](https://img.shields.io/badge/Linux-172033?style=flat-square&logo=linux&logoColor=67E8A5)
![Docker](https://img.shields.io/badge/Docker-172033?style=flat-square&logo=docker&logoColor=67E8A5)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-172033?style=flat-square&logo=postgresql&logoColor=67E8A5)
![Redis](https://img.shields.io/badge/Redis-172033?style=flat-square&logo=redis&logoColor=67E8A5)
![PyTorch](https://img.shields.io/badge/PyTorch-172033?style=flat-square&logo=pytorch&logoColor=67E8A5)

</div>

---

## `04 / elsewhere`

- **Problem solving:** 500+ DSA problems solved on LeetCode
- **LinkedIn:** [linkedin.com/in/Vishal-V-ab8a2131b](https://linkedin.com/in/Vishal-V-ab8a2131b/)
- **Email:** [vv14022006@gmail.com](mailto:vv14022006@gmail.com)

<div align="center">

<sub><code>principle.txt</code> — I prefer understanding why a system behaves the way it does, not just making it run.</sub>

</div>
