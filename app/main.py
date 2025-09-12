"""Módulo principal da aplicação FastAPI EasyOrder."""

# External libraries
from fastapi import FastAPI
from app.routers import pedidos

# Internal libraries
from app.routers.pedidos import router as pedidos_router
from app.routers.clientes import router as clientes_router
from app.database import Base, engine

app = FastAPI()
app.include_router(pedidos.router)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="EasyOrder API",
    description="API para gerenciamento de pedidos e clientes.",
    version="1.0.0",
)


@app.get("/")
def read_root():
    """
    Rota raiz da API.

    Returns:
        dict: Mensagem de boas-vindas.
    """
    return {"message": "Bem-vindo ao EasyOrder!"}


app.include_router(pedidos_router, prefix="/pedidos", tags=["Pedidos"])
app.include_router(clientes_router, prefix="/clientes", tags=["Clientes"])