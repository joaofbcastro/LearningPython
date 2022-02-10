from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
if jogador <= 2:
    sleep(0.7)
    print('JO')
    sleep(0.7)
    print('KEN')
    sleep(0.7)
    print('PÔ!!!')
    sleep(0.7)
    print('-='*14)
    print('O Jogador Jogou:    {}.'.format(itens[jogador]))
    print('O Computador Jogou: {}.'.format(itens[computador]))
    print('-='*14)
    if computador == 0:
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('O Jogador GANHOU!')
        elif jogador == 2:
            print('O Jogador PERDEU!')
    elif computador == 1:
        if jogador == 0:
            print('O Jogador PERDEU!')
        elif jogador == 1:
            print('EMPATE!')
        elif jogador == 2:
            print('O Jogador GANHOU!')
    elif computador == 2:
        if jogador == 0:
            print('O Jogador GANHOU!')
        elif jogador == 1:
            print('O Jogador PERDEU!')
        elif jogador == 2:
            print('EMPATE!')
    print('')
else:
    print('')
    print('Opção invalida, tente novamente')
