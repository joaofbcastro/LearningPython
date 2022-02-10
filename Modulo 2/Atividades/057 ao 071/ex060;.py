# Mostrar o fatorial de um número de
c = número = int(input('Digite um número para calcular o seu fatorial: '))
f = 1
print('Calculando {}! = '.format(número), end='')
while c > 0:
    print('{}'.format(c), end='')
    f *= c
    c -= 1
    print(' x ' if c != 0 else ' = ', end='')
print(f)
