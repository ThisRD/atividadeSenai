
#36 - Crie um programa que pede que o usuário digite um nome ou uma frase, verifique se esse conteúdo digitado é um palíndromo ou não, exibindo em tela esse resultado.

from os import system
system('cls')

palavra = input("Digite uma palavra: ")
palavra = palavra.replace(' ','').upper()
revertida = palavra[::-1]
print(palavra,revertida)
palindromo = True

for i in range(len(palavra)):
    if (palavra[i]!=revertida[i]):
        palindromo = False
        break
if palindromo:
    print("é um palindromo")
else:
    print("Não é um palindromo")