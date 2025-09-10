"""Esquemas Pydantic para validação de dados da API."""

from pydantic import BaseModel

class PedidoBase(BaseModel):
    """Schema base para pedidos."""

    descricao: str


class PedidoCreate(PedidoBase):
    """Schema de criação de pedidos."""
    pass


class Pedido(PedidoBase):
    """Schema de leitura de pedidos."""

    id: int
    cliente_id: int

    class Config:
        orm_mode = True


class ClienteBase(BaseModel):
    """Schema base para clientes."""

    nome: str
    email: str


class ClienteCreate(ClienteBase):
    """Schema de criação de clientes."""
    pass


class Cliente(ClienteBase):
    """Schema de leitura de clientes."""

    id: int
    pedidos: list[Pedido] = []

    class Config:
        orm_mode = True
