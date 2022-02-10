'''lista = [2, 5, 9, 1]
lista[2] = 3
lista.append(7)
# lista.sort()
lista.sort(reverse=True)
lista.insert(2, 0)
lista.pop(2)
print(lista)
print(f'Essa lista tem {len(lista)} elementos.')'''

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for pos, value in enumerate(valores):
    print(f'Na posição {pos} encontrei o valor {value}!')
print('Cheguei ao final da lista!')
