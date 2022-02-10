'''cinquenta = vinte = dez = um = 0
saque = int(input('Quanto você quer sacar? R$'))
 
if saque // 50 != 0:
    print(f'Total de {saque // 50} notas de R$50,00')
    saque -= (saque // 50)*50
if saque // 20 != 0:
    print(f'Total de {saque // 20} notas de R$20,00')
    saque -= (saque // 20)*20
if saque // 10 != 0:
    print(f'Total de {saque // 10} notas de R$10,00')
    saque -= (saque // 10)*10
if saque // 1 != 0:
    print(f'Total de {saque // 1} notas de R$1,00')
    saque -= (saque // 1)*1
'''