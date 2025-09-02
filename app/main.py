"""Módulo principal da aplicação EasyOrder com FastAPI."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def hello_world():
    """Retorna uma mensagem de boas-vindas para teste de rota básica."""
    return {"mensagem": "Olá, mundo! Bem-vindo ao EasyOrder."}
