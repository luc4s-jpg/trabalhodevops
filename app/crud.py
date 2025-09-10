"""Funções CRUD para clientes e pedidos."""

from sqlalchemy.orm import Session
from app import models, schemas


# Clientes
def criar_cliente(db: Session, cliente: schemas.ClienteCreate) -> models.Cliente:
    """Cria um novo cliente no banco de dados."""
    db_cliente = models.Cliente(**cliente.model_dump())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente


def listar_clientes(db: Session, skip: int = 0, limit: int = 10) -> list:
    """Lista todos os clientes com paginação."""
    return db.query(models.Cliente).offset(skip).limit(limit).all()


def obter_cliente(db: Session, cliente_id: int) -> models.Cliente | None:
    """Obtém um cliente pelo ID."""
    return db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()


# Pedidos
def criar_pedido(
    db: Session, pedido: schemas.PedidoCreate, cliente_id: int
) -> models.Pedido:
    """Cria um novo pedido associado a um cliente."""
    db_pedido = models.Pedido(**pedido.model_dump(), cliente_id=cliente_id)
    db.add(db_pedido)
    db.commit()
    db.refresh(db_pedido)
    return db_pedido


def listar_pedidos(db: Session, skip: int = 0, limit: int = 10) -> list:
    """Lista todos os pedidos com paginação."""
    return db.query(models.Pedido).offset(skip).limit(limit).all()


def obter_pedido(db: Session, pedido_id: int) -> models.Pedido | None:
    """Obtém um pedido pelo ID."""
    return db.query(models.Pedido).filter(models.Pedido.id == pedido_id).first()
