print('Bem vindo ao digitador de números!\nDigite \033[31m999\033[m para parar.\n')
cont = soma = 0
while True:
    número = int(input('Digite um número: '))
    if número == 999:
        break
    cont += 1
    soma += número
print(f'\nA soma dos {cont} números é igual a {soma}.')
