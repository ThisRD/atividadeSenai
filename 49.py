from os import system
system('cls')

aluno = [{"Nome" : "Fernando", "Notas" : [62,73,90]}]

def mediaAluno(aluno):
    notas = []
    for media in aluno :
        if len(media["Notas"]) > 0 :
            temp = round(sum(media["Notas"]) / len(media["Notas"]))
        else:
            temp = 0
        notas.append({"Nome" : media["Nome"]})