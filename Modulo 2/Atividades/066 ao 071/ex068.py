from random import randint


cont = 0
traço = '-='*15
print(f'{traço}\nVamos jogar Par ou Ímpar!\n{traço}')
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()

    # Verifique se deu par ou ímpar.
    resultado = 'P' if (jogador + computador) % 2 == 0 else 'I'
    print(f'Você jogou {jogador} e o computador {computador}. Total de \033[32m{jogador+computador}\033[m!')

    # Se errou, interrompa!
    if not escolha in resultado:
        print(f'{traço}\n\033[31mVocê Perdeu!\033[m\n{traço}\nGame Over! Você venceu {cont} vezes!\n')
        break

    # Se não, conte um acerto e reinicie.
    cont += 1
    print(f'{traço}\n\033[32mVocê Acertou!\033[m\nVamos Jogar novamente...\n{traço}')

