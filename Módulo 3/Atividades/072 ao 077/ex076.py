lista = (
    'Pão', 2.50,
    'Pera', 2.35,
    'Maçã', 8.99,
    'Batata', 6.79,
    'Melancia', 10.50,
    'Manga', 5.30
)
print('-'*38)
print(f'{"LISTA DE PREÇOS":^38}')
print('-'*38)
for pos in range(len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}R${lista[pos + 1]:>7.2f}')
