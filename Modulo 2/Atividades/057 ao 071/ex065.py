#
count = soma = média = maior = menor = 0
parar = 'S'
while parar in 'Ss':
    n = int(input('Digite um número: '))
    count += 1
    soma += n
    if count == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    parar = str(input('\033[35mQuer continuar?\033[m [S/N]: '))
média = soma / count
print('\n\033[32mVocê inseriu {} números.\nA soma entre eles é {}.\nA média foi {:.2f}.\nO maior entre os valores foi {} e o menor foi {}.\033[m\n'.format(count, soma, média, maior, menor))
