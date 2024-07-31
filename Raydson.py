#Dev's name: Raydson Silva
#Date: 18/06/2024
#Name Project: Calculo de média 
from os import system
system('cls')

aluno = [{"Nome" : "Raydson" , "Notas" : [40,58]}]

def calculoMedia(aluno):
    notas = []
    for media in aluno:
        if len(media["Notas"]) > 50:
            temp = round(sum(media["Notas"]) / len(media["Notas"]))
            print("Você passou!\n")
        else:
            temp = round(sum(media["Notas"]) / len(media["Notas"]))
            print("Você não passou!\nFicara de recuperação!\n")

        notas.append({"Nome" : media["Nome"], "Médiadas Notas" : temp})
    print(notas)

mediaAluno = calculoMedia(aluno)


