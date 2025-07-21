import os

from langchain_openai import OpenAI, ChatOpenAI
from dotenv import load_dotenv
from langchain_community.cache import InMemoryCache
from langchain.globals import set_llm_cache

load_dotenv(dotenv_path=".env.development")

openapi_key = os.getenv("OPENAI_API_KEY")

model = OpenAI()

set_llm_cache(InMemoryCache())

prompt = "Quém foi Alan Turing?"

response1 = model.invoke(prompt)
print(response1)

response2 = model.invoke(prompt)
print(response2)
