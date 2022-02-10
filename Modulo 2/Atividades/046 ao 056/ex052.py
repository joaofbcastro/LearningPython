# Verifica se o números é primo
núm = int(input('\nDigite um número: '))
tot = 0
for c in range(1, núm + 1):
    if núm % c == 0:
        print('\033[36m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} pode ser vividido {} vezes.'.format(núm, tot))
if tot == 2:
    print('O número {} é um número primo.\n'.format(núm))
else:
    print('O número {} não é um número primo.\n'.format(núm))
