#47 – Crie um dicionário usando o construtor de dicionários do Python, alimente os valores do mesmo com os dados de duas listas:

from os import system
system('cls')

produtos = ['Arroz','Feijão','Macarrão',"Carne"]
preços = [20,10,12.5,35]

lista_compras = dict(zip(produtos,preços))

print(lista_compras)