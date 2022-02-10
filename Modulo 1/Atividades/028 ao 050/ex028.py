from random import randint
from time import sleep
aleatorio = randint(0, 5)
print(' ')
print('Pensando em um número entre 0 e 5...')
chute = int(input('Qual número você acha que eu escolhi? '))
print('Pensando...')
sleep(2)
print('{:^45}'.format("-:-"*17))
if chute == aleatorio:
    print('Caramba! Eu realmente pensei no número {}, como você soube?'.format(aleatorio))
else:
    print('Tente novamente. Desta vez eu pensei no número {}.'.format(aleatorio))
print('{:^45}'.format("-:-"*17))
