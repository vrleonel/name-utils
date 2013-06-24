import sqlalchemy as sa
from models import Base

def criar_tabelas(url_bd):
    engine = sa.create_engine(url_bd, echo=True)
    Base.metadata.create_all(engine)

if __name__=='__main__':
    url_bd = 'sqlite:///nomes.sqlite'
    criar_tabelas(url_bd)
