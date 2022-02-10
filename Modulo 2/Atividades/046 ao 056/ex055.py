# Maior e menor sequencia
print('-=' * 16)
for c in range(5):
    peso = float(input(f'[{c+1}] - Qual o seu peso em quilos? '))
    if c == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('\nO maior peso inserido foi {:.2f}Kg.'.format(maior))
print('O menor peso inserido foi {:.2f}Kg.'.format(menor))
print('-=' * 26)
