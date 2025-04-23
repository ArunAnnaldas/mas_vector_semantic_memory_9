# 🤖 Multi-Agent Workflow with Semantic Memory (LangChain + OpenAI + FAISS)

This project implements a **multi-agent AI system** that collaborates through shared semantic memory. Each agent has a specific role — Planner, Developer, and Critic — and they work together to break down, implement, and review tasks.

Built using:
- 🧠 LangChain (v0.2+)
- ✨ OpenAI GPT-3.5
- 🗂 FAISS (for semantic memory)
- 📊 `tiktoken` (token usage tracking)
- 🔁 Reflexive retry and contextual chaining

---

## 👥 Agent Roles

| Agent | Role |
|-------|------|
| 🧠 **Planner Agent** | Breaks user request into subtasks |
| 💻 **Developer Agent** | Generates code using previous steps from memory |
| 🧐 **Critic Agent** | Reviews code and provides improvements |
| 🔁 **Reflexive Loop** | If feedback includes "improve", Developer retries automatically |

---

## 🔁 Features

✅ Role-specific agents  
✅ Shared semantic memory using FAISS  
✅ Clean agent output formatting  
✅ Auto token usage display per agent  
✅ Per-agent logging under `/logs/`  
✅ Reflexive retry loop  
✅ LangChain v0.2+ compatible (`.invoke`, `.content`, etc.)

---


---

## 🧠 Semantic Memory

Agents store and retrieve semantically relevant context using `VectorStoreRetrieverMemory` with FAISS, allowing:
- Flexible phrasing across turns
- Recall of concepts across agents
- Memory-based prompt enrichment

---

## 🚀 How to Run

### 1. Install Dependencies

```bash
pip install langchain langchain-openai langchain-community openai faiss-cpu tiktoken


📊 Logs
Each agent logs:

Prompt
Response
Token usage

You’ll find them under logs/ folder, separated by agent.
