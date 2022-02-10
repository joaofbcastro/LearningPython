lista = []
for c in range(5):
    lista.append(int(input('Digite um número: ')))
print(f'Você digitou os valores: {lista}')

maior = sorted(lista)[len(lista)-1]
menor = sorted(lista, reverse=True)[len(lista)-1]
maior_p = []
menor_p = []
for pos, x in enumerate(lista):
    if x == maior:
        maior_p.append(str(pos))
    if x == menor:
        menor_p.append(str(pos))

print(f'O maior valor digitado foi {maior} nas posições {", ".join(maior_p)}.')
print(f'O menor valor digitado foi {menor} nas posições {", ".join(menor_p)}.')
