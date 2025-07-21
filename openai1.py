import os

from langchain_openai import OpenAI, ChatOpenAI
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env.development")

openapi_key = os.getenv("OPENAI_API_KEY")

# client = OpenAI(api_key=openapi_key)
#
#
# response = client.invoke(
#     input="Explique com riqueza de detalhes quem foi Alan Turing",
#     temperature=0.5,
#     max_tokens=250,
# )
#
# print(response)

model = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=openapi_key,
    temperature=0.5,
)

messages = [
    {'role': 'system', 'content': 'You are a helpful assistant.'},
    {'role': 'user', 'content': 'Explique com riqueza de detalhes quem foi Alan Turing'}
]

response = model.invoke(messages)

print(response)
print(response.content)
