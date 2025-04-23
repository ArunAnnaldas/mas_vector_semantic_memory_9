from langchain_openai import ChatOpenAI
from memory.faiss_store import memory
from utils.logger import log_interaction
from utils.token_counter import count_tokens

llm = ChatOpenAI(temperature=0)

def planner_agent(task):
    response = llm.invoke(f"Break the following task into implementation steps:\n{task}")
    memory.save_context({"input": task}, {"output": response})
    token_info = count_tokens(task, response)
    log_interaction("planner", task, response, token_info)
    return response