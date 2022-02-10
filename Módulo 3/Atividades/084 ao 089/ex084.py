users = list()
while True:
    Nome = str(input('\033[32mNome: \033[m'))
    Peso = float(input('\033[32mPeso: \033[m'))
    users.append([Nome, Peso])
    resp = str(input('\033[33mQuer continuar? [S/N]: \033[m')).strip().upper()[0]
    if resp =='N':
        break
print(f'\nForam cadastradas {len(users)} pessoas no total.')
pesos = list()
leves = list()
pesados = list()
for pessoa in users:
    pesos.append(pessoa[1])
maxpeso = max(pesos)
minpeso = min(pesos)
for pessoa in users:
    if pessoa[1] == maxpeso:
        pesados.append(pessoa[0])
    if pessoa[1] == minpeso:
        leves.append(pessoa[0])
print(f'As pessoas mais pesadas foram: {", ".join(pesados)}. Pesando {maxpeso}Kg.')
print(f'As pessoas mais leves foram: {", ".join(leves)}. Pesando {minpeso}Kg.')
