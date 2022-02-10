# Mostra os 10 primeiros números de uma Progressão Aritmética.
print('='*30)
print('{: ^30}'.format('10 TERMOS DE UMA PA'))
print('='*30)
primeiro = int(input('Insira o primeiro termo: '))
razão = int(input('Insira o valor da razão: '))
progressão = primeiro
for c in range(10):
    print(progressão, end=' → ')
    progressão += razão
print("Acabou")
