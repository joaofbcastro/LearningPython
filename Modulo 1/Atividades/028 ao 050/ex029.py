print(' ')
v = int(input('A quantos Km/h você está dirigindo? '))
print(' ')
if v > 80:
    multa = (v - 80) * 7
    print('Opa, você está acima da velocidade permitida.')
    print('Você terá de pagar R$7.00 por Km/h execido.')
    print('-'*35)
    print('Aqui está o recivbo da sua multa:')
    print('Km/h excedidos:      {}Km/h'.format(v-80))
    print('Valor da multa:      R${:.2f}'.format(multa))
    print(' ')
print('Tenha um ótimo dia! Diriga com segurança.')
print('')