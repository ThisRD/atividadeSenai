#3) Crie um programa usando a estrutura “faça enquanto” que leia vários números.
#A cada laço, pergunte se o usuário quer continuar ou não. No final, mostre na tela:
#a) O somatório entre todos os valores
#b) Qual foi o menor valor digitado
#c) A média entre todos os valores
#d) Quantos valores são pares

i = 1
soma = 0
media = 0
cont_numero = 0
par = 0
im = 1

while (i != 0):
    numero = int(input('Digite um numero: '))
    continuar = input('Você deseja continuar? ')
    soma += numero
    cont_numero += 1
    media = (media + numero) / cont_numero
    if (im != 0 ):
        menor_numero = numero
        im = im - 1
    if (numero < menor_numero):
        menor_numero = numero
    if (numero %2 == 0):
        par = par + 1
    if (continuar == 'sim') or (continuar =='s'):
        i = 1
    else:
        i = 0

   
print('A soma entre os valores é {};'.format(soma))
print('O menor numero digitado é {};'.format(menor_numero))
print('A média enre os valores é {};'.format(media))
print('{} numeros são pares!'.format(par))

