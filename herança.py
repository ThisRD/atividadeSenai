class Pet(object):
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def getNome(self):
        return self.nome
    def setIdade(self, idade):
        return self.idade(idade)
    def som(self):
        pass
    
class Cachorro(Pet):
    def __init__(self,nome,idade):
        super().__init__(nome,idade)
        print(f'Parabéns eu sou {self.nome} e tenho {self.idade} anos de idade')
    def som(self):
        return 'au au'
    
class Gato(Pet):
    def __init__(self,nome,idade):
        super().__init__(nome,idade)
        print(f'Parabéns eu sou {self.nome} e tenho {self.idade} anos de idade')
    def som(self):
        return 'miau miau'
    
class Peixe(Pet):
    def __init__(self,nome,idade):
        super().__init__(nome,idade)
        print(f'Parabéns eu sou {self.nome} e tenho {self.idade} anos de idade')
    def som(self):
        return 'glub glub'
    # super = superior
caramelo = Cachorro('caramelo',10)
print(caramelo.som())
mingau = Gato('mingau',7)
print(mingau.som())
dourado = Peixe('dourado',5)
print(dourado.som())