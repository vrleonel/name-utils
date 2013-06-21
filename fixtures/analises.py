#!/usr/bin/env python3

from zipfile import ZipFile

def nao_separador(linha):
    return len(set(linha.strip())) != 1

with ZipFile('isen2006.txt.zip') as entrada_zip:
    print('lendo...')
    with entrada_zip.open('isen2006.txt') as entrada:
        linhas = []
        for lin in filter(nao_separador, entrada):
            print(lin)
            linhas.append(lin)

    print(len(linhas), 'linhas lidas')

