#Dev's name: Raydson Silva
#Date: 18/06/2024
#Name Project: Calculo de média 
from os import system
system('cls')
print("escreva a lista de alunos, como escrita abaixpo\nartur\njoão\ncaue")

nome = [input("Nomes dos alunos:\n"),input(),input()]
notas = [[int(input("Notas dos alunos:\nlopal ")), int(input("ler "))], [int(input("lopal ")) ,int(input("ler "))], [int(input("lopal ")), int(input("ler "))]]

aluno = dict(zip(nome,notas))


for chave,valor in aluno.items():
    if (aluno.values(1,2,3f)) > 50 :
        print(aluno)