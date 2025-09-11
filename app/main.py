"""Módulo principal da aplicação EasyOrder com FastAPI."""

from fastapi import FastAPI
from app.routers import pedidos


app = FastAPI()
app.include_router(pedidos.router)

@app.get("/hello")
def hello_world():
    """Retorna uma mensagem de boas-vindas para teste de rota básica."""
    return {"mensagem": "Olá, mundo! Bem-vindo ao EasyOrder."}
