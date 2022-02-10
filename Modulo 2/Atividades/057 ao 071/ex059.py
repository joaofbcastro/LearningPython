# Menu
from time import sleep

n1 = int(input('\n\033[32mBem vindo ao CalcPower.\033[m\nDigite um número:   '))
n2 = int(input('Digite outro valor: '))
opção = 0
while opção != 5:
    opção = int(input('\nMenu\nO que deseja fazer com os valores?\n[1] Somar\n[2] Multiplicar\n[3] Mostrar o maior\n[4] Inserir novos números\n[5] Sair do CalcPower\n\nEscolha uma opção: '))
    if opção == 1:
        resposta = 'A soma dos valores é igual a {}.'.format(n1 + n2)
    elif opção == 2:
        resposta = 'O resultado de {} multiplicado por {} é {}.'.format(
            n1, n2, n1 * n2)
    elif opção == 3:
        maior = n1
        if n2 > maior:
            maior = n2
        resposta = 'O maior número entre {} e {} é {}.'.format(n1, n2, maior)
    elif opção == 4:
        n1 = int(input('Insira um novo número:    '))
        n2 = int(input('Insira outro novo número: '))
        resposta = '\n{} e {} são os novos valores.'.format(n1, n2)
    elif opção == 5:
        print('\033[31mDesligando tudo...')
        sleep(1)
        resposta = 'Até a proxima!'
    else:
        resposta = '\033[31mEssa opção não existe.'
    print('\033[32m{}\033[m'.format(resposta))
    sleep(1)
