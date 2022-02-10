# Como eu fiz
'''from random import randint

cont = 0
lista = ("")
for c in range(5):
    cont += 1
    n = randint(0, 9)
    if cont == 1:
        maior = menor = n
    elif n < menor:
        menor = n
    elif n > maior:
        maior = n
    lista += (f' {n}')

print(f'Os números sorteados foram:{lista}')
print(f'O maior número sorteado foi {maior}')
print(f'O menor número sorteado foi {menor}')'''

# COmo ensinou no vídeo

from random import randint

lista = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), )
print('Os números sorteador foram:', end='')
for num in lista:
    print(f' {num}', end='')
print(f'\nO maior número sorteado foi {max(lista)}')
print(f'O menor número sorteado foi {min(lista)}')
