#7) [DESAFIO] Vamos melhorar o jogo que fizemos no exercício 32. A partir de agora, o computador vai sortear um número entre 1 e 10 e o jogador vai ter 4 tentativas para tentar acertar

n = 0
while  n < 4 :
    import random 
    numero = random.randint(1,10)
    numero_jogador = int(input('Digite um numero entre 1 e 10:'))
    if (numero == numero_jogador):
        print('Parabéns, você acertou')
        n = 4
    else :
        print('Você errou, tente novamente!')
        n = n + 1
    if (n == 4):
        print('O numero sorteado era {}!'.format(numero))