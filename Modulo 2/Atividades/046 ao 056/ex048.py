# A soma de todos os nímeros impares que são multiplos de três e se encontram no intervalo de 1 até 500
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma dos valores solicitados é {}.'.format(soma))
print('Foram somados {} números.'.format(cont))
