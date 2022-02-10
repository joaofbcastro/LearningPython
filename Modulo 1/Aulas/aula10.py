# Condições

nota1 = float(input('Quanto foi a sua primeira nota? '))
nota2 = float((input('E a segunda nota? ')))
média = (nota1 + nota2) / 2
if média >= 6:
    print('Pelos meus calculos {:.1f} está dentro da média.'.format(média))
else:
    print('Parece que você não foi muito bem nesse bimestre. Estudo mais!')
print('-'*28)
