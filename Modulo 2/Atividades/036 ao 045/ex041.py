from datetime import date

nascimento = int(input('Qual o ano em que você nasceu? '))
idade = (date.today().year)-nascimento

if 0 < idade <= 9:
    categoria = 'Mirim'
elif idade <= 14:
    categoria = 'Infantil'
elif idade <= 19:
    categoria = 'Junior'
elif idade <= 25:
    categoria = 'Sênior'
elif idade > 25:
    categoria = 'Monster'

print('O atleta tem {} anos e se encaixa na na categoria {}.'.format(idade, categoria))
