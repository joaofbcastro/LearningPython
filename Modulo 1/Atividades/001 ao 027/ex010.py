# Carteira
saldo = float(input('Quantos reais você tem na carteira? R$'))
print('----------------')
print('Com R${:.2f} você poderá comprar US${:.2f}.'.format(saldo, (saldo / 3.27)))
print('Levando em consideração que US$1,00 vale R$3,27.')
print('----------------')
