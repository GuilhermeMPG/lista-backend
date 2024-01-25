from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base


class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(30))
    email = Column(String(40), unique=True)
    senha = Column(String(60))
    ativo = Column(Boolean)
    admin = Column(Boolean)    
    dia_fatura = Column(Integer)
    listaDeDesejos = relationship('ItemDesejo')
    faturas = relationship('Fatura')


class ItemDesejo(Base):
    __tablename__ = "itemDesejo"
    id= Column(Integer, primary_key=True, index=True)
    nome= Column(String(30))
    descricao= Column(String(30))
    prioridade= Column(Integer)
    preco= Column(Float)
    adquirido= Column(Boolean)
    usuario_id= Column(Integer, ForeignKey('usuario.id', name='fk_usuario_itemDesejo'))


class Fatura(Base):
    __tablename__ = "fatura"
    id= Column(Integer, primary_key=True, index=True)
    nomeInstituicao= Column(String(30))
    nomeFatura= Column(String(30))
    valor= Column(Float)
    parcelas= Column(Integer)
    usuario_id= Column(Integer, ForeignKey('usuario.id', name='fk_usuario_fatura'))
