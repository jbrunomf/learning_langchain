import os

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env.development")

openapi_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model="gpt-3.5-turbo")

template = ''''
Traduza o texto do {idioma_origem} para o {idioma_destino}: {texto}
'''

prompt_template = PromptTemplate.from_template(template=template)

prompt = prompt_template.format(
    idioma_origem='português',
    idioma_destino='francês',
    texto='Oi, tudo bem?'
)

response = model.invoke(prompt)

print(response)