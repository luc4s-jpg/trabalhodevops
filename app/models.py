"""Modelos de dados do sistema EasyOrder."""

# External libraries
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

# Own libraries
from app.database import Base


class Cliente(Base):
    """Modelo para clientes."""

    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    pedidos = relationship("Pedido", back_populates="cliente")


class Pedido(Base):
    """Modelo para pedidos."""

    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))

    cliente = relationship("Cliente", back_populates="pedidos")
