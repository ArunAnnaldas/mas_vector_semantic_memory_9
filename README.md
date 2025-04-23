# 🤖 Multi-Agent Workflow with Shared Semantic Memory (LangChain + FAISS)

This project implements a collaborative multi-agent system using LangChain and FAISS. The system includes a Planner, Developer, and Critic agent — all sharing semantic memory via a FAISS vector store.

## 👥 Agent Roles

- **Planner Agent**: Breaks user request into subtasks
- **Developer Agent**: Generates code from the plan
- **Critic Agent**: Reviews the generated code

## 🧠 Features

- Role-specialized agents
- Shared memory via VectorStoreRetrieverMemory
- FAISS for fast semantic retrieval
- Token-efficient execution using GPT-3.5

## 🚀 How to Run

```bash
pip install langchain langchain-openai langchain-community openai faiss-cpu tiktoken
export OPENAI_API_KEY="your-key-here"
python main.py
```

## 📁 Project Structure

```
multi_agent_workflow/
├── main.py
├── agents/
│   ├── planner.py
│   ├── developer.py
│   └── critic.py
├── memory/
│   └── faiss_store.py
└── README.md
```
