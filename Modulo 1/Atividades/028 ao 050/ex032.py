# Ano bissexto

from datetime import date
print(' ')
year = int(input('Digite um ano qualquer: '))
if year == 0:
    year = date.today().year
print('-'*35)
rest = year % 4
if rest == 0 and year % 100 != 0 or year % 400 == 0:
    print('O ano de {} é um ano Bissexto.'.format(year))
else:
    print('O ano de {} não é um ano Bissexto.'.format(year))
print(' ')
