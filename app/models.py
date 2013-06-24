from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class Nome(Base):
    __tablename__ = 'nomes'

    id = Column(String, primary_key=True)
    nome = Column(String, unique=True)
    nome_normalizado = Column(String, unique=True) # nome sem acentos, todo em caixa baixa


