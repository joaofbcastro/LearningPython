maiores = homens = mulheres_jovens = 0

while True:
    idade = int(input('\nQual a sua idade? '))
    # Verifica se o valor é válido.
    while True:
        sexo = str(
            input('Qual o seu sexo? \033[34m[F/M]\033[m ')).strip().upper()
        if sexo in 'FM':
            break
    # Soma os valores nas váriaveis.
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if idade <= 20 and sexo == 'F':
        mulheres_jovens += 1
    print('\033[32mDados contabilizados!\033[m')
    # Verifica se o valor é válido.
    while True:
        continuar = str(input('Você quer continuar? \033[32m[S/N]\033[m ')).strip().upper()
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
print(
    f'\nFim do programa!\nTotal de pessoas com mais de 18 anos: {maiores}.\nAo todo foram cadastrados {homens} homens.\nE {mulheres_jovens} mulheres com menos de 20 anos.')
