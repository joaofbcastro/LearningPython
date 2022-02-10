# Sequencia de Fibonacci
print('-'*35)
print('Sequência de Fibonacci')
print('-'*35)
quantidade = int(input('Quantos termos você quer ver? '))
Fn = n1 = 0
n2 = 1
print('~'*35)
while quantidade != 0:
    print(Fn, end=', ')
    quantidade -= 1
    Fn = n1 + n2
    n2 = n1
    n1 = Fn
print('Fim!')
print('~'*35)
