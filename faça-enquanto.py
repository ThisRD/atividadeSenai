
#2) Faça um programa usando a estrutura “faça enquanto” que leia a idade de várias pessoas. A cada laço, você deverá perguntar para o usuário se ele quer ou não continuar a digitar dados. No final, quando o usuário decidir parar, mostre na tela:
#a) Quantas idades foram digitadas
#b) Qual é a média entre as idades digitadas
#c) Quantas pessoas tem 21 anos ou mais.

i = 10000000000000000000000000000000000000000000000000
media = 0 
cont_idade = 0
cont_21 = 0

while (i != 0):
    idade = int(input('Digite a sua idade = '))
    continuar = input('Você deseja continuar o seu cadastro? ')
    cont_idade += 1
    media = (media + idade) / cont_idade
    if (idade >= 21):
        cont_21 += 1
    if (continuar == 'sim'):
        i = i - 1
    else :
        i = 0 
        print('Obrigado, tenha um bom dia!')
print('Foram digitadas {} idades;'.format(cont_idade))
print('A média entre as idades digitads foi de {};'.format(media)) 
print('{} pessoas têm mais 21 anos ou mais!'.format(cont_21))
if (cont_21 == 0):
    print('Ninguem tem 21 anos ou mais!')
