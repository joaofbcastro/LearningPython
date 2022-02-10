# Impar ou par

print(' ')
n = int(input('Digite um número: '))
resto = n % 2
print('-'*35)
if resto == 0:
    print('O número {} é PAR.'.format(n))
else:
    print('O npumero {} é IMPAR.'.format(n))
print(' ')
