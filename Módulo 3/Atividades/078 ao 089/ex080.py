lista = []
count = 0
for c in range(5):
    num = int(input('Digite um valor: '))
    # se for a primeira ocorrência ou se o numero for maior que o maior da lista.
    if c == 0 or num > lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            # se o numero for menor que algum da lista, ele adiciona e encerra.
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1
print(lista)
