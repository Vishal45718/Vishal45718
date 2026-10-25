<!--
  Vishal Varukolu — GitHub Profile README
  Live profile snapshot: assets/profile-dashboard.svg
  Generator: scripts/generate_profile_dashboard.py
  Schedule:  .github/workflows/profile-dashboard.yml
  Images in assets/: IITH.png, contact-cat.png, cat_1.png
  Badge palette: background 172033, logo/accent 67E8A5 (matches the dashboard)
-->

<div align="center">

<img src="./assets/IITH.png" width="120" alt="Indian Institute of Technology Hyderabad logo"/>

# Vishal Varukolu

**CSE @ IIT Hyderabad · Class of 2027**

`systems` · `backend infrastructure` · `compilers` · `applied ML`

<br/>

<a href="https://github.com/Vishal45718">
  <img src="./assets/profile-dashboard.svg" width="100%" alt="Terminal-style GitHub dashboard showing public repositories, stars, forks, and followers"/>
</a>

<sub><code>vishal@iith:~$ ./profile --snapshot</code> · public GitHub metrics · refreshed daily</sub>

</div>

---

## `01 / whoami`

I like working close to the metal and tracing problems across the stack, from compiler passes and data structures to distributed services and GPU training systems.

| | |
|:--|:--|
| **Currently building** | Tools for reasoning about failures in distributed training |
| **Engineering philosophy** | Small, testable components; explicit trade-offs; measurements over unbenchmarked claims of scale |

---

## `02 / selected-work`

### TrainPulse
*Research · Distributed training observability*

Co-developed a lightweight fault-localization pipeline for multi-node LLM training. It combines iteration-time change detection, component-level anomaly scores, and dependency-aware reasoning to narrow down likely sources of fail-slow behavior.

- **100% single-fault localization accuracy**
- **Under 1% runtime overhead**, compared with **2.18%** for the PyTorch profiler
- Evaluated on a **4-node cluster** fine-tuning **Llama 3 8B**

**Stack:** `Python` · `PyTorch DDP` · `Distributed GPU training`

> Under submission to ACM SIGMETRICS 2027. The research code is not public yet; contact me for details.

### [LAOP Compiler](https://github.com/Vishal45718/LAOP-compiler)
*Compiler backend*

A domain-specific compiler for linear-algebra expressions. The backend performs semantic checks and emits Eigen-based C++ code, with matrix-chain ordering as an optimization pass.

**Stack:** `C++` · `Eigen`

### [Self-Healing RAG](https://github.com/Vishal45718/Self_Healing_RAG)
*Retrieval and evaluation*

A RAG pipeline that can critique its own response path: reformulate a query, retry grounded generation, or abstain when the evidence is weak. Includes an evaluation harness for comparison against baseline retrieval.

**Stack:** `Python` · `LangGraph` · `ChromaDB` · `Sentence Transformers`

### [Scalable Recommendation System](https://github.com/Vishal45718/Scalable_Recommendation_System)
*Backend and data infrastructure*

An event-driven recommendation-system project exploring Kafka ingestion, vector retrieval with FAISS, and a Redis-backed feature cache.

**Stack:** `FastAPI` · `Kafka` · `FAISS` · `Redis` · `PostgreSQL`

### [Inventory Management System](https://github.com/Vishal45718/IMS_Full-Stack-Inventory-Management-System)
*Full-stack web application*

A multi-branch inventory application with REST APIs, JWT authentication, role-based access, and relational data constraints around stock and orders.

**Stack:** `Go` · `Gin` · `MySQL` · `Next.js`

---

## `03 / toolchain`

<div align="center">

**Languages**<br/>
![C++](https://img.shields.io/badge/C%2B%2B-172033?style=flat-square&logo=cplusplus&logoColor=67E8A5)
![Python](https://img.shields.io/badge/Python-172033?style=flat-square&logo=python&logoColor=67E8A5)
![Go](https://img.shields.io/badge/Go-172033?style=flat-square&logo=go&logoColor=67E8A5)
![TypeScript](https://img.shields.io/badge/TypeScript-172033?style=flat-square&logo=typescript&logoColor=67E8A5)
![SQL](https://img.shields.io/badge/SQL-172033?style=flat-square&logo=mysql&logoColor=67E8A5)

**Systems and infrastructure**<br/>
![Linux](https://img.shields.io/badge/Linux-172033?style=flat-square&logo=linux&logoColor=67E8A5)
![Docker](https://img.shields.io/badge/Docker-172033?style=flat-square&logo=docker&logoColor=67E8A5)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-172033?style=flat-square&logo=postgresql&logoColor=67E8A5)
![Redis](https://img.shields.io/badge/Redis-172033?style=flat-square&logo=redis&logoColor=67E8A5)

**Machine learning**<br/>
![PyTorch](https://img.shields.io/badge/PyTorch-172033?style=flat-square&logo=pytorch&logoColor=67E8A5)

</div>

---

## `04 / elsewhere`

**Problem solving:** 500+ DSA problems solved on LeetCode

<div align="center">

<a href="https://linkedin.com/in/Vishal-V-ab8a2131b/">
  <img src="https://img.shields.io/badge/LinkedIn-connect-172033?style=flat-square&labelColor=172033" alt="Connect on LinkedIn"/>
</a>
<a href="mailto:vv14022006@gmail.com">
  <img src="https://img.shields.io/badge/Email-say_hello-172033?style=flat-square&labelColor=172033" alt="Email Vishal"/>
</a>

<br/><br/>

<a href="mailto:vv14022006@gmail.com">
  <img src="./assets/contact-cat.png" width="200" alt="A surprised ginger cat holding a telephone handset"/>
</a>

<sub><strong>Operator standing by.</strong> Happy to talk systems, infrastructure, compilers, and applied ML.</sub>

</div>

---

<div align="center">

<a href="https://github.com/Vishal45718">
  <img src="./assets/cat_1.png" width="200" alt="A curious cat looking into the camera"/>
</a>

<sub><code>exit 0</code> · Thanks for visiting my corner of GitHub.</sub>

<sub><code>principle.txt</code> · I prefer understanding why a system behaves the way it does, not just making it run.</sub>

</div>
