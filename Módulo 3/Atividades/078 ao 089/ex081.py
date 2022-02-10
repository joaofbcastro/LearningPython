lista = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    continuar = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(
    f'Você inseriu {len(lista)} números.',
    f'\nOs valores em ordem decrescente são: {sorted(lista, reverse=True)}.',
    '\nO valor 5 não foi encontrado na lista.' if not 5 in lista else '\nO valor 5 foi encontrado na lista.'
)

