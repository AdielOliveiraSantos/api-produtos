from sqlalchemy import column, BigInteger, String, Numeric, CheckConstraint, Integer, DateTime, Column
from sqlalchemy.sql.functions import current_timestamp

from app import db

class Produto(db.Model):

    __tabelename__ = 'produto'

    id = Column(BigInteger, primary_key=True)
    nome = Column(String(128), nullable=False)
    preco = Column(Numeric(10, 2), CheckConstraint('preco >= 0.0'), nullable=False, server_default="0.0")
    quantidade = Column(Integer, CheckConstraint('quantidade >= 0'), nullable=False, server_default="0")

    criado_em = Column(DateTime, server_default=current_timestamp())
    modificado_em = Column(
        DateTime,
        server_default=current_timestamp(),
        onupdate=current_timestamp()
    )

    def __init__(self, nome: str= "", preco: float = 0.0, quantidade: int = 0) -> None:
        self.name = nome
        self.preco = preco
        self.quantidade = quantidade


    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return f'<Produto: {self.nome}>'