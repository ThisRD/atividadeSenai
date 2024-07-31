#45 – A partir da seguinte lista [‘C’, ‘JavaScript’, ‘Lua’, ‘Python’] verifique primeiramente e retorne ao usuário se a linguagem de programação Python consta na lista. Retorne uma mensagem amigável ao 
# usuário para estas duas situações:

from os import system
system('cls')
#First form(Recomended)
linguagens = ["C", "JavaScript", "Lua", "Python"]
if "Python" in linguagens:
    print("Python está na lista")
else:
    print("Python não está na lista")
#Second form(not recomended)
    stay = False
for i in linguagens:
    if i == "Python":
        stay = True
        break
if (stay):
    print("Python está na lista")
else:
    print("Não está na lista")