lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(
    f'\nVocê digitou os números: {lista}',
    f'\nOs números pares são: {pares}',
    f'\nOs números impares são: {impares}'
)
