from langchain_openai import ChatOpenAI
from memory.faiss_store import memory
from utils.logger import log_interaction
from utils.token_counter import count_tokens

llm = ChatOpenAI(temperature=0)

def developer_agent(task):
    docs = memory.retriever.get_relevant_documents(task)
    context = "\n".join([doc.page_content for doc in docs])
    prompt = f"Based on this plan, write Python code:\n{context}"
    response = llm.invoke(prompt)
    memory.save_context({"input": prompt}, {"output": response})
    token_info = count_tokens(prompt, response)
    log_interaction("developer", prompt, response, token_info)
    return response