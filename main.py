from fastapi import FastAPI
from models import TextRequest, load_text_model, generate_text


app = FastAPI()

#carregamento
model = load_text_model()


#rota 1
@app.get("/")
def status():
    return {"message": "OK!"}


#retorno da tradução
@app.post("/translate")
def translate(data: TextRequest):
    text = generate_text(model, data.prompt)
    return {"translation_text": text}