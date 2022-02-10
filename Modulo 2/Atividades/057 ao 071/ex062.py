# Termos de uma PA porém melhor
termo = int(input('Digite um termo: '))
razão = int(input('Digite a razão: '))
cont = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont < total:
        print(termo, end=' -> ')
        termo += razão
        cont += 1
    print('Pausa!')
    mais = int(input('Você quer ver mais quantos termos dessa PA? '))
print('\nVocê viu {} termos dessa PA.'.format(total))
