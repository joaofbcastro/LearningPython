# Jogo de adivinhar número
from random import randint

tentativas = 1
acertou = False
aleatorio = randint(0, 10)
print('\033[34m\nBem vindo ao Guru Virtual\033[36m')
print('Estou escolhendo um número entre 0 e 10...\033[m')
chute = int(input('Que número eu escolhi? '))
while chute != aleatorio:
    tentativas += 1
    proximidade = 'maior'
    if chute > aleatorio:
        proximidade = 'menor'
    chute = int(input('\033[31mErrou! tente um número\033[33m {}.\033[m\nQue número eu escolhi? '.format(proximidade)))
    if chute == aleatorio:
        acertou = True
print('\033[32m\nCaramba! Eu realmente pensei no número \033[33m{}\033[32m, como você soube?\033[35m\nNúmero de tentativas: \033[33m{}.\033[m'.format(aleatorio, tentativas))
