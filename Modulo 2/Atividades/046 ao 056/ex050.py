# sei la que merda é essa
s = 0
cont = 0
for c in range(3):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
        cont += 1 
if cont != 0:
    print('Você inseriu {} números pares, a soma deles é igual a {}.'.format(cont, s))
else:
    print('Você não inseriu números Pares.')
