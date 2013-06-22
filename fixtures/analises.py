#!/usr/bin/env python3

from zipfile import ZipFile
import itertools
from operator import itemgetter, eq

def nao_separador(linha):
    return len(set(linha.strip())) != 1

def primeiro_nome(linha):
    return linha.split()[1]

dic_nomes = {}

with ZipFile('isen2006.txt.zip') as entrada_zip:
    with entrada_zip.open('isen2006.txt') as entrada:
        gen_nomes = (primeiro_nome(s.decode('utf-8')) for s in
                        filter(nao_separador, entrada))
        for nome, ocorrencias in itertools.groupby(gen_nomes):
            qtd = len(list(ocorrencias))
            dic_nomes[nome] = qtd

# nomes que só aparecem uma vez
'''
print(len(
          list(
               filter(
                      lambda n: n==1,
                      dic_nomes.values()))))

'''
# nomes que aparecem ao menos 100 vezes
'''
print(len(
          list(
               filter(
                      lambda n: n>=100,
                      dic_nomes.values()))))

'''
nomes_por_ocorrencias = sorted(dic_nomes.items(), key=itemgetter(1))
for nome, qtd in itertools.chain(itertools.islice(nomes_por_ocorrencias, 100),
                                 itertools.islice(nomes_por_ocorrencias,
                                    len(nomes_por_ocorrencias)-100,
                                    len(nomes_por_ocorrencias))):
    print(nome)
