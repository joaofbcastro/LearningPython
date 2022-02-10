n = int(input('Digite um número até 9999: '))
m = n // 1000 % 10
c = n // 100 % 10
d = n // 10 % 10
u = n // 1 % 10
print('Milhar:  {}'.format(m))
print('Centena: {}'.format(c))
print('Dezena:  {}'.format(d))
print('Unidade: {}'.format(u))
