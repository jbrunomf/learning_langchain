import os

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env.development")

openapi_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model="gpt-3.5-turbo")

chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage("Responda as perguntas com o conhecimento de um geografo especialista no Brasil"),
        HumanMessagePromptTemplate.from_template('Me explique os aspectos geograficos da região {regiao}'),
        AIMessage('Certo, irei analisar a sua solicitação, um momento.'),
        HumanMessage('Inclua também informações relacionadas que forem importantes.'),
        AIMessage('Ok, aqui estão as informações solicitadas: ')
    ]
)

prompt = chat_template.format(regiao='Norte do Brasil')

response = model.invoke(prompt)

print(response.content)
