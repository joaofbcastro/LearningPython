n = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite outro numero: '))
print('')
if n > n2:
    print('O maior número é o {} e o menor é o {}.'.format(n, n2))
elif n2 == n:
    print('Não existe valor maior pois {} é igual a {}.'.format(n, n2))
else:
    print('O maior número é o {} e o menor é o {}.'.format(n2, n))
print('')
