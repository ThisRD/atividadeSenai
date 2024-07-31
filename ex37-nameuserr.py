#declare uma variável que por sua vez recebe um nome digitado
#pelo usuário, emseguida, exiba em tela uma mensagem de boas vindas 
#que incorpora o nome anteriormente digitado, fazendo uso de f"strings

from os import system
system('cls')

nome = input("Digite o seu nome: ")
print(f"Olá {nome} seja muito bem-vindo(a)!")