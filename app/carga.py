import sqlalchemy as sa
from models import Base
import io, sys
def criar_tabelas(url_bd):
    engine = sa.create_engine(url_bd, echo=True)
    Base.metadata.create_all(engine)

def carregar(url_bd, nome_arq):
	engine = sa.create_engine(url_bd, echo=True)
	with io.open(nome_arq, encoding='utf-8') as entrada:
		for n, lin in enumerate(entrada, 1):
			print(n, lin)

if __name__=='__main__':
    url_bd = 'sqlite:///nomes.sqlite'
    #criar_tabelas(url_bd)
    carregar(sys.argv[1])
