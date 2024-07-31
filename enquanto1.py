#5) Crie um algoritmo que leia a idade de 10 pessoas, mostrando no final:
#a) Qual é a média de idade do grupo
#b) Quantas pessoas tem mais de 18 anos
#c) Quantas pessoas tem menos de 5 anos
#d) Qual foi a maior idade lida
maior_idade=0
menor_idade=0
soma_idade = 0
midade=0
n = 0

while (n < 10):
    idade = int(input("Digite sua idade:"))
    soma_idade+=idade
    if (idade > 18):
        maior_idade+=1
    if (idade < 5):
        menor_idade+=1 
    if (midade<idade):
        midade = idade 
    n+=1
print('Média de idades lidas:',(soma_idade/n))
print('Pessoas com mais de 18 anos:',maior_idade)
print('Pessoas com menos de 5 anos:',menor_idade)
print('maior idade lida:',midade)