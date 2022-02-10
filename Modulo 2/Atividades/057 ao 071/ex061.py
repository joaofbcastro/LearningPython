# Termos de uma PA
acumulado = termo = int(input('Primeiro termo: '))
razão = int(input('Razão da PA:    '))
contador = 10
while contador != 0:
    print(acumulado, end='\033[32m -> \033[m')
    acumulado += razão
    contador -= 1
print('FIM\n')
