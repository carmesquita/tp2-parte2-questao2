import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel


#Modelo dos dados recebidos pela API
class TextRequest(BaseModel):
    prompt: str

#carregamento do modelo
def load_text_model():
    model = ChatOpenAI(model="openai/gpt-oss-20b", api_key=os.environ["GROQ_API_KEY"], base_url="https://api.groq.com/openai/v1")
    return model

#tradução do texto
def generate_text(model, prompt):
    template = PromptTemplate(template="Translate this text from English into {language}. Return only the translation. Text: {sentence}", input_variables=["sentence", "language"])
    chain = template | model
    response = chain.invoke({"sentence": prompt, "language": "French"})
    return response.content