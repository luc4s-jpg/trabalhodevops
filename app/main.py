from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello_world():  # função sem docstring e linha longa proposital para violar as regras
    return {"mensagem": "Olá, mundo! Esta mensagem ultrapassa os 90 caracteres para testar o linting"}
