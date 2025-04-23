from langchain_openai import ChatOpenAI
from memory.faiss_store import memory
from utils.logger import log_interaction
from utils.token_counter import count_tokens

llm = ChatOpenAI(temperature=0)

def critic_agent(code):
    prompt = f"Review the following Python code and suggest improvements if needed:\n{code}"
    response = llm.invoke(prompt)
    memory.save_context({"input": prompt}, {"output": response})
    token_info = count_tokens(prompt, response)
    log_interaction("critic", prompt, response, token_info)
    return response