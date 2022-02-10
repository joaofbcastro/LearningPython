matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = somaColuna3 = 0
for c1 in range(len(matriz)):
    for c2 in range(len(matriz[c1])):
        matriz[c1][c2] = int(input(f'Digite um valor para [{c1}, {c2}]: '))
        if matriz[c1][c2] % 2 == 0:
            somaPares += matriz[c1][c2]
        if matriz[c1][c2] == 2:
            somaColuna3 += matriz[c1][c2]
print('-='*15)
for c in range(len(matriz)):
    print(f'[{matriz[c][0]:^6}] [{matriz[c][1]:^6}] [{matriz[c][2]:^6}]')
print(
    '-='*15,
    f'\nA soma de todos os valores pares é {somaPares}.',
    f'\nA soma de todos os valores da terceira coluna é {somaColuna3}.',
    f'\nO maior valor da segunda linha é {max(matriz[1])}.'
)
