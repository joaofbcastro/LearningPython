# Custo da viagem

print(' ')
distance = int(input('Qual a distancia da viagem, em km: '))
print(' ')
if distance <= 200:
    coast = 0.50
    price = 'R${:.2f}'.format(distance * coast)
else:
    coast = 0.45
    price = 'R${:.2f}'.format(distance * coast)
print('O seu custo será de R${} por Km percorrido.'.format(coast))
print('O preço total da sua viagem é {}.'.format(price))
print(' ')
