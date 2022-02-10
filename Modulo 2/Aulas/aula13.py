'''moeda = True

for c in range(1,6):
    if moeda:
        print('Peguei a moeda')
    print(f'Passo [{c}]')
if moeda:
    print('Pegando a ultima moeda')
print('Último passo')
print('Pegando a maçã\nFim\n')'''


n = int(input('Digite um número: '))
for c in range(1, n+1):
    print("{:2}".format(c))
print('\nFim\n')
