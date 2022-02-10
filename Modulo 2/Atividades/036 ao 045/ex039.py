from datetime import date

print('')

atual = date.today().year
nasc = int(input('Digite o ano em que você nasceu: '))
idade = atual - nasc

tempo = 'anos'
if idade - 18 <= 1:
    tempo = 'ano'

if idade < 18:
    print('Você ainda tem {} anos, terá de se alistar em {} {}.'.format(
        idade, (18 - idade), tempo))
elif idade > 18:
    print('Você já tem {} anos, você deveria ter se alistado hà {} {}.'.format(
        idade, (idade - 18), tempo))
elif idade == 18:
    print('Está na hora de se alistar, você já tem 18 anos.')

print('')
