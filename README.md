<!--
  Vishal Varukolu — GitHub Profile README
  Profile: https://github.com/Vishal45718
  Optional enhancement: add a generated SVG dashboard at assets/profile-terminal.svg.
-->

<div align="center">

# Vishal Varukolu

**CSE @ IIT Hyderabad · Class of 2027**

*Systems · Backend Infrastructure · Compilers · Applied ML*

<br/>

<a href="mailto:vv14022006@gmail.com">
  <img src="https://img.shields.io/badge/Email-Contact-1f6feb?style=flat-square&logo=gmail&logoColor=white" alt="Email"/>
</a>
<a href="https://linkedin.com/in/Vishal-V-ab8a2131b/">
  <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"/>
</a>
<a href="https://github.com/Vishal45718">
  <img src="https://img.shields.io/badge/GitHub-Vishal45718-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub"/>
</a>

</div>

---

## `whoami`

I like working close to the metal and tracing problems across the stack — from compiler passes and data structures to distributed services and GPU training systems.

- **Interests:** systems, backend infrastructure, compilers, applied ML
- **Currently building:** tools for reasoning about failures in distributed training
- **Engineering mindset:** small, testable components; explicit trade-offs; and measurements over claims of scale without benchmarks

---

## Selected work

### 01 · TrainPulse
**Research · Distributed training observability**

Co-developed a lightweight fault-localization pipeline for multi-node LLM training. It combines iteration-time change detection, component-level anomaly scores, and dependency-aware reasoning to narrow down likely sources of fail-slow behavior.

> **Reported evaluation:** 100% single-fault localization accuracy with under 1% runtime overhead, compared with 2.18% overhead for the PyTorch profiler.

Evaluated on a 4-node cluster fine-tuning Llama 3 8B.

**Stack:** `Python` · `PyTorch DDP` · Distributed GPU training

*Under submission to ACM SIGMETRICS 2027. The research code is not public yet; contact me for details.*

---

### 02 · [LAOP Compiler](https://github.com/Vishal45718/LAOP-compiler)
**Compiler backend · C++**

A domain-specific compiler for linear-algebra expressions. The backend performs semantic checks and emits Eigen-based C++ code, with matrix-chain ordering as an optimization pass.

**Stack:** `C++` · `Eigen`

---

### 03 · [Self-Healing RAG](https://github.com/Vishal45718/Self_Healing_RAG)
**Retrieval and evaluation · Python**

A RAG pipeline that can critique its own response path: reformulate a query, retry grounded generation, or abstain when the evidence is weak. Includes an evaluation harness for comparison against baseline retrieval.

**Stack:** `Python` · `LangGraph` · `ChromaDB` · `Sentence Transformers`

---

### 04 · [Scalable Recommendation System](https://github.com/Vishal45718/Scalable_Recommendation_System)
**Backend / data infrastructure · Python**

An event-driven recommendation-system project exploring Kafka ingestion, vector retrieval with FAISS, and a Redis-backed feature cache.

**Stack:** `FastAPI` · `Kafka` · `FAISS` · `Redis` · `PostgreSQL`

---

### 05 · [Inventory Management System](https://github.com/Vishal45718/IMS_Full-Stack-Inventory-Management-System)
**Full-stack · Go + web**

A multi-branch inventory application with REST APIs, JWT authentication, role-based access, and relational data constraints around stock and orders.

**Stack:** `Go` · `Gin` · `MySQL` · `Next.js`

---

## Tools I use

<div align="center">

![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)

</div>

---

## A little beyond projects

- **Problem solving:** 500+ DSA problems solved on LeetCode
- **LinkedIn:** [linkedin.com/in/Vishal-V-ab8a2131b](https://linkedin.com/in/Vishal-V-ab8a2131b/)
- **Email:** [vv14022006@gmail.com](mailto:vv14022006@gmail.com)

---

<div align="center">

*I prefer understanding why a system behaves the way it does—not just making it run.*

</div>
