# app_with_favicon.py
from fastapi import FastAPI
from fastapi.responses import Response
from mineru.api import app as mineru_app  # importa o app original do MinerU

app = FastAPI()

# Monta o app principal do MinerU dentro do nosso wrapper
app.mount("/", mineru_app)

# Adiciona o favicon vazio
@app.get("/favicon.ico")
def favicon():
    return Response(content=b"", media_type="image/x-icon")
