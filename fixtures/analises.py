
from zipfile import ZipFile

with ZipFile('isen2006.txt.zip') as entrada:
	print('lendo...')
	txt = entrada.read('isen2006.txt')
	txt = txt.decode('utf-8')
	linhas = txt.split('\n')
	print(len(linhas), 'linhas lidas')
	
