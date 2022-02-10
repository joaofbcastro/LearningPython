tabela = ("Atlético-MG", "Flamengo", "Palmeiras", "Fortaleza", "Corinthians", "Bragantino", "Fluminense", "América-MG", "Atlético-GO",
          "Santos", "Ceará", "Internacional", "São Paulo", "Athletico-PR", "Cuiabá", "Juventude", "Grêmio", "Bahia", "Sport", "Chapecoense")

# Mostra apenas os 5 primeiros colocados.
print('====  Os 5 primeiros colocados são:  ====')
for pos, time in enumerate(tabela[:5]):
    print(f'{pos + 1 :0>2} - {time}')

# Mostra apenas os 4 últimos colocados.
print('\n====  Os 4 últimos colocados são:  ====')
for pos, time in enumerate(tabela[-4:]):
    print(f'{pos + 1 :0>2} - {time}')

# Lista dos times em ordem alfabética.
print('\n====  Os times em ordem alfabética são: ====')
for pos, time in enumerate(sorted(tabela)):
    print(f'{pos + 1 :0>2} - {time}')

print(
    f'\n====  A Chapecoense está na {tabela.index("Chapecoense") + 1}ª posição da tabela  ====\n')
