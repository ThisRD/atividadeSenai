#46 – A partir de um simples dicionário composto por três itens, {‘Alto Nível’: ‘Python, ‘Médio Nível’: ’C’, ‘Baixo Nível’: ‘Assembly’}, verifique se ‘Python’ consta no dicionário em questão, utilizando de negação lógica para tal verificação:


from os import system
system('cls')

nivel= {
    "Alto Nível": "Python", 
    "Médio Nível": "C", 
    "Baixo Nível": "Assembly"
}

stay = False
for chave,valor in nivel.items():
    if not valor != "Python":
        stay = True
if stay :
    print("Python está presente")
else:
    print("Python não está presente")