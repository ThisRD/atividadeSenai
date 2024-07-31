#1. Crie um programa que realiza a contagem de 0 a 50, em progressão aritmética exibindo apenas os números ímpares, sendo que a razão é 3:

#Exemplo de saída: "0,3,9,15,21..."
from os import system
system('cls')

termo = 0
razão = 3 
for i in range(termo, 51, razão):   #Loop da contagem
    if i % 2 != 0:                  #Verifica se os termos são impares e exibe no teminal
        print(i, end = ' ')
print('\n')        


#2.Crie um programa que exibe em tela a tabuada de um determinado número fornecido pelo usuário, e o usuário também determine até qual termo a tabuada vai calcular, por ex:

#P: Digite qual tabuada você quer?
#R: 5
#P: Até qual termo você quer calcular?
#R: 7

#Exemplo de saída:
#5x1=5
#5x2=10
#5x3=15
#5x4=20
#5x5=25
#5x6=30
#5x7=35

numero = int(input("Digite qual tabuda você quer?\n"))
term = int(input("Até qual termo?\n"))

for num in range(1,term + 1):
    if num <= term :
        print(f"{numero} X {num} = {numero * num}")

#3. Crie um programa que realiza a contagem de 1 até 999, usando apenas de números pares, ao final do processo exiba em tela quantos números pares foram encontrados nesse intervalo, assim como a soma dos mesmos:

#Exemplo de saída:
#1
#2
#4
#6
#8
#10
#...
soma = 0
cont = 0    
for i in range(1,1000):
    if i % 2 == 0 :   
        print(i)
        soma += i
        cont += 1
print(f"{cont} números pares foram contados, com {soma} sendo a soma entre eles")