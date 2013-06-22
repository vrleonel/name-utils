#!/usr/bin/env python3

from zipfile import ZipFile
import itertools
from operator import itemgetter

def nao_separador(linha):
    return len(set(linha.strip())) != 1

def primeiro_nome(linha):
    return linha.split()[1]

dic_nomes = {}

with ZipFile('isen2006.txt.zip') as entrada_zip:
    print('lendo...')
    with entrada_zip.open('isen2006.txt') as entrada:
        gen_nomes = (primeiro_nome(s.decode('utf-8')) for s in
                        filter(nao_separador, entrada))
        for nome, ocorrencias in itertools.groupby(gen_nomes):
            qtd = len(list(ocorrencias))
            print(nome, qtd)
            dic_nomes[nome] = qtd

for nome, qtd in sorted(dic_nomes.items(), key=itemgetter(1)):
    print(nome, qtd)

