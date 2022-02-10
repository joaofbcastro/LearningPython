# Analise de idade
from datetime import date

ano_atual = date.today().year
print(f'Estamos no ano de {ano_atual}')

print("-=" * 20)
maiores = 0
menores = 0
for c in range(7):
    nascimento = int(input(f'[{c+1}] Qual o seu ano de nascimento? '))
    idade = ano_atual - nascimento
    print('   Quam nasceu em {} tem {} anos.'.format(nascimento, idade))
    if idade >= 21:
        maiores += 1
    elif idade < 21:
        menores += 1
print(f'\n{maiores} pessoas já atingiram 21 anos e {menores} são menores de 21 anos.')
print("-=" * 28)
