import os
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_anthropic import ChatAnthropic
from langchain.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")  
os.environ['ANTHROPIC_API_KEY'] = ANTHROPIC_API_KEY

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    return vector_store

def get_conversational_chain(vector_store):
    llm = ChatAnthropic(
        model="claude-3-haiku-20240307",
        api_key=ANTHROPIC_API_KEY,
        temperature=0.7,
        max_tokens=1000
    )
    
    # Custom prompt template to ensure English responses
    prompt_template = """
    You are a helpful assistant that answers questions based on the provided context. 
    Always respond in English, regardless of the language of the question.
    
    Use the following context to answer the question concisely in maximum 2-3 paragraphs. 
    Keep your response brief and to the point.
    If the answer is not available in the provided context, say "The answer is not available in the context provided."
    Do not make up information that is not in the context.
    
    Context: {context}
    
    Chat History: {chat_history}
    
    Question: {question}
    
    Answer in English (maximum 2-3 paragraphs):"""
    
    PROMPT = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "chat_history", "question"]
    )
    
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm, 
        retriever=vector_store.as_retriever(), 
        memory=memory,
        combine_docs_chain_kwargs={"prompt": PROMPT}
    )
    return conversation_chain