matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c1 in range(len(matriz)):
    for c2 in range(len(matriz)):
        matriz[c1][c2] = int(input(f'Digite um valor para [{c1}, {c2}]: '))
print('-='*15)
for c in range(len(matriz)):
    print(
        f'[{matriz[c][0]:^6}] [{matriz[c][1]:^6}] [{matriz[c][2]:^6}]'
    )
