#44 – Crie um dicionário via método construtor dict( ), atribuindo para o mesmo ao menos 5 conjuntos de chaves e valores representando objetos e seus respectivos preços:

from os import system
system('cls')

precos = dict(
    {
        "Deladeira":1500,
        "Fogão":600,
        "jogoPratos":700,
        "Escumadeira":15,
        "Frigideira":30
    }
)
print(precos)
