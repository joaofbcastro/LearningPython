from random import randint
from time import sleep


palpites = []
amount = int(input('Quantos jogos você quer gerar? '))
print(f'{f" Sorteando {amount} números ":=^31}')

for c in range(amount):
    count = 0
    # Adiciona um número aleatorio caso o número ainda não esteja na lista.
    while True:
        número = f'{randint(0, 60):2}'
        if número not in palpites:
            palpites.append(número)
            count += 1
        if count == 6:
            break
    sleep(0.5)
    print(f'Jogo {c+1}: {", ".join(sorted(palpites))}.')
    palpites.clear()

print(f'{" Boa sorte! ":=^31}')
