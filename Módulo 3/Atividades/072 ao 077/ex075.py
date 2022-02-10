valor = (int(input('Digite um valor: ')),
         int(input('Digite outro valor: ')),
         int(input('Digite mais um valor: ')),
         int(input('Digite o último valor: ')))
if 9 in valor:
    if valor.count(9) > 1:
        print(f'O número 9 apareceu {valor.count(9)} vezes.')
    else: 
        print(f'O número 9 apareceu {valor.count(9)} vez.')
if 3 in valor:
    print(f'O número 3 apareceu na {valor.index(3)+1}ª posição.')
pares = ''
for n in valor:
    if n % 2 == 0:
        pares += f' {n}'
if pares != '':
    if len(pares) > 2:
        print(f'Os números pares inseridos foram:{pares}.')
    else:
        print(f'O único número par inserido foi:{pares}.')
