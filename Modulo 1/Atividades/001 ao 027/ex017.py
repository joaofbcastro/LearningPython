# Caucula o comprimento da hipotenusa

from  math import hypot
print('-' * 30)
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('E o cateto adjacente: '))

hipo = hypot(ca, co)
# hipo = (ca ** 2 + co ** 2) ** (1/2)

print('-' * 30)
print('O comprimento da hipotenusa de seu triangulo retangulo é: {:.2f}'.format(hipo))
