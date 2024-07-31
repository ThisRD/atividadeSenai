#39 - Dada a seguinte lista: nomes = [‘Ana’, ‘Carlos’, ‘Daiane’, ‘Fernando’, ‘Maria’], substitua o terceiro elemento da lista por ‘Jamile’:
#40 - Adicione o elemento ‘Paulo’ na lista nomes:
#41 - Adicione o elemento ‘Eliana’ na lista nomes, especificamente na terceira posição da lista:
#42 - Remova o elemento ‘Carlos’ da lista nomes:
#43 - Mostre o segundo, terceiro e quarto elemento da lista nomes. Separadamente, mostre apenas o último elemento da lista nomes:

from os import system
system('cls')

nomes = ["Ana", "Carlos", "Daiane", "Fernando", "Maria"]
nomes[2]= "Jamili"
print(nomes)
nomes.append("Paulo")
print(nomes)
nomes.insert(2,"Eliana")
print(nomes)
nomes.remove("Carlos")
print(nomes)
print(nomes[1],nomes[2],nomes[3])
print(nomes[1:4])
print(nomes[-1])