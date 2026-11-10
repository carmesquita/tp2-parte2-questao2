# TP2 Parte 2 Questão 2 — Tradução com LangChain

## Objetivo

API com FastAPI que recebe um texto em inglês e retorna sua tradução para o francês usando LangChain.
Utilizei ChatOpenAI com o modelo openai/gpt-oss-20b pela Groq.

## Arquivos

- `main.py`: cria a aplicação e define as rotas.
- `models.py`: define a entrada, configura o modelo e realiza a tradução.
- `teste_modelo.py`: testa a tradução pelo terminal.
- `requirements.txt`: registra as bibliotecas e suas versões.
- `README.md`: apresenta as instruções de execução e teste.

## Como executar

Com o Python instalado, abra o terminal dentro da pasta do projeto.

Crie o ambiente virtual:
python -m venv .venv

Instalação das bibliotecas utilizadas:
.\.venv\Scripts\python.exe -m pip install -r requirements.txt

É necessário ter uma chave da Groq. No terminal PowerShell, configure sua chave:
$env:GROQ_API_KEY = "SUA_CHAVE"

Inicialização:
.\.venv\Scripts\python.exe -m uvicorn main:app --port 8001

## Como testar

Para testar diretamente pelo terminal:
.\.venv\Scripts\python.exe teste_modelo.py

Para testar pela API, com a aplicação iniciada, acesse:
http://127.0.0.1:8001/docs

Abra POST /translate, clique em Try it out, informe o JSON abaixo e clique em Execute:
{"prompt": "The cat is on the table."}
O retorno esperado é um JSON com o campo translation_text e a tradução para o francês.

## Dificuldade encontrada

A página da Groq permaneceu em carregamento e não consegui criar a chave de API. Por isso, deixei o código preparado, mas não consegui realizar os testes de tradução e verificar o tempo de resposta.

## Sobre o uso de IA
Usei ChatGPT como apoio para ajudar na elaboração do código e conferencias. 