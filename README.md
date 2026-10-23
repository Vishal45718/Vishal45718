# Vishal Varukolu

CSE @ IIT Hyderabad · 2027

I like working close to the metal and tracing problems across the stack — from compiler passes and data structures to distributed services and GPU training systems.

- **Interests:** systems, backend infrastructure, compilers, applied ML
- **Currently building:** tools for reasoning about failures in distributed training
- **Contact:** [Email](mailto:vv14022006@gmail.com) · [LinkedIn](https://linkedin.com/in/Vishal-V-ab8a2131b/)

---

## Selected work

### TrainPulse
*Research · Distributed training observability*

Co-developed a lightweight fault-localization pipeline for multi-node LLM training. It combines iteration-time change detection, component-level anomaly scores, and dependency-aware reasoning to narrow down likely sources of fail-slow behavior.

Evaluated on a 4-node cluster fine-tuning Llama 3 8B, the reported results were **100% single-fault localization accuracy with under 1% runtime overhead**, compared with 2.18% overhead for the PyTorch profiler.

**Stack:** Python · PyTorch DDP · distributed GPU training

*Under submission to ACM SIGMETRICS 2027. The research code is not public yet; contact me for details.*

### [LAOP Compiler](https://github.com/Vishal45718/LAOP-compiler)
*Compiler backend · C++*

A domain-specific compiler for linear-algebra expressions. The backend performs semantic checks and emits Eigen-based C++ code, with matrix-chain ordering as an optimization pass.

**Stack:** C++ · Eigen

### [Self-Healing RAG](https://github.com/Vishal45718/Self_Healing_RAG)
*Retrieval and evaluation · Python*

A RAG pipeline that can critique its own response path: reformulate a query, retry grounded generation, or abstain when the evidence is weak. Includes an evaluation harness for comparison against baseline retrieval.

**Stack:** Python · LangGraph · ChromaDB · Sentence Transformers

### [Scalable Recommendation System](https://github.com/Vishal45718/Scalable_Recommendation_System)
*Backend / data infrastructure · Python*

An event-driven recommendation-system project exploring Kafka ingestion, vector retrieval with FAISS, and a Redis-backed feature cache.

**Stack:** FastAPI · Kafka · FAISS · Redis · PostgreSQL

### [Inventory Management System](https://github.com/Vishal45718/IMS_Full-Stack-Inventory-Management-System)
*Full-stack · Go + web*

A multi-branch inventory application with REST APIs, JWT authentication, role-based access, and relational data constraints around stock and orders.

**Stack:** Go · Gin · MySQL · Next.js

---

## Tools I use

`C++` · `Python` · `Go` · `TypeScript` · `SQL` · `Linux` · `Docker` · `PostgreSQL` · `Redis` · `PyTorch`

I prefer small, testable components, explicit trade-offs, and measurements over claims of scale without benchmarks.

---

## Elsewhere

- LeetCode — 500+ DSA problems solved
- [LinkedIn](https://linkedin.com/in/Vishal-V-ab8a2131b/)
- [Email](mailto:vv14022006@gmail.com)
