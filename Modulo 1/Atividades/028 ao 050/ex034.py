print(' ')
wage = float(input('Qual o valor do seu salário atual? R$'))
if wage > 1250.00:
    increase = wage * 0.10
else:
    increase = wage * 0.15
print('-'*40)
print('O valor do seu aumento será de R${:.2f}'.format(increase))
print('Seu novo salário será:         R${:.2f}'.format(wage + increase))
print(' ')
