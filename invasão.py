class cachorro(object):
    def __init__(self,nome,anoNasc):
        self.nome = nome
        self.anoNasc = anoNasc
        print(f"Parabens eu sou{self.nome} seu novo cachorro")
    
    def som(self):
        print(f"{self.nome} late")
    
    def getIdade(self):
        return 2024 - self.anoNasc
    def setAnoNasc(self,ano):
        self.anoNasc = ano
        
# caramelo = cachorro('caramelo',2010)
# caramelo.som()
# idadeCaramelo =  caramelo.getIdade()
# print('Idade : ', idadeCaramelo)
caraDeChinelo = cachorro('cara de chinelo',2010)
print('Idade:',caraDeChinelo.getIdade())
caraDeChinelo.setAnoNasc(2023)
print('Idade:',caraDeChinelo.getIdade())
caraDeChinelo.anoNasc = 2021
print('Idade:',caraDeChinelo.getIdade())
print('ano nascimento:',caraDeChinelo.anoNasc)
#print('Idade : ', idadeCaraDeChinelo)
#caraDeChinelo.som()


class gato(object):
    def __init__(self,nome,anoNasc):
        self.nome = nome
        self.anoNasc = anoNasc
        print(f"Parabens sou {self.nome} seu novo gato")
        
    def som(self):
        print(f"{self.nome} mia")
        
    def getIdade(self):
        return 2024 - self.anoNasc
        
# nino = gato('nino',2015)
# idadeNino = nino.getIdade()
# print('Idade : ', idadeNino)
# nino.som()
# mingau = gato('mingau',2020)
# idadeMingau = mingau.getIdade()
# print('Idade:',idadeMingau)
# mingau.som()