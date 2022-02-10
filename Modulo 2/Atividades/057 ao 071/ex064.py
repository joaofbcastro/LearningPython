# Para quando digitar 000
count = soma = n = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        count += 1
        soma += n
print('A soma dos {} números digitados é igual a {}.\n'.format(count, soma))
