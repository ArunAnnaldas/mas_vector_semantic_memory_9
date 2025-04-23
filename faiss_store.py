from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.memory import VectorStoreRetrieverMemory
from langchain.schema import Document

def init_memory():
    embedding_model = OpenAIEmbeddings()
    docs = [Document(page_content="Initial memory for agent collaboration.")]
    vectorstore = FAISS.from_documents(docs, embedding_model)

    global memory
    memory = VectorStoreRetrieverMemory(
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        memory_key="history"
    )
    return memory