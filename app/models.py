"""Modelos de dados do sistema EasyOrder."""

# External libraries
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime


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


class Produto(Base):
    """Modelo para produtos."""

    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False)
    preco = Column(Integer, nullable=False)
    categoria = Column(String, index=True, nullable=False)
    qtdEstoque = Column(Integer, nullable=False)


class Entrega(Base):
    """Modelo para entregas."""

    __tablename__ = "entregas"

    id = Column(Integer, primary_key=True, index=True)
    endereco = Column(String, index=True, nullable=False)
    status = Column(String, index=True, nullable=False)
    data_entrega = Column(DateTime, nullable=False, default=datetime.now)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"), nullable=False)
