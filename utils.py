from langchain_ollama import ChatOllama
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()

base_url = 'http://localhost:11434'
llm = ChatOllama(model='llama3.2',base_url=base_url)

groq_llm = ChatGroq(model='llama-3.2-11b-vision-preview')

def poem_generator(question):
    prompt = "You are an expert in writing poems, so write a poem based on the user's question."

    chains = ChatPromptTemplate.from_template(prompt)
    print(chains)

    response = llm.invoke(question)
    # print(response)
    return response.content

def code_generator(question):
    prompt = "You are an expert in Programming, so code a Program based on the user's question."

    chains = ChatPromptTemplate.from_template(prompt)
    print(chains)

    response = groq_llm.invoke(question)
    # print(response)
    return response.content

