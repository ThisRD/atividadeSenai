def mostrar_contagem():
    # Inicializa o contador
    contador = 0
    
    # Loop para contar de 0 a 18, de 3 em 3
    while contador <= 18:
        print(contador, end=' ')
        contador += 3
    
    # Mensagem de término
    print("Acabou!")

# Chamada da função para mostrar a contagem
mostrar_contagem()




def contagem_ate(numero):
    contador = 1  # Inicializa o contador
    while contador <= numero:
        print(contador, end=' ')
        contador += 1
    print("Acabou!")

# Solicita ao usuário um número inteiro e positivo
numero = int(input("Digite um valor inteiro e positivo: "))

# Verifica se o número fornecido é positivo
if numero <= 0:
    print("O número fornecido não é positivo.")
else:
    print("Contagem:", end=' ')
    contagem_ate(numero)