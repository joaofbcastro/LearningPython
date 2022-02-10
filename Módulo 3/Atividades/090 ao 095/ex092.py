from datetime import datetime

year = datetime.now().year

ficha = {}

ficha["nome"] = name = str(input('Nome: '))
birth = int(input('Ano de nascimento: '))
ficha["idade"] = age = year - birth
ctps = int(input('Nº da carteira de trabalho (0 não tem): '))
if ctps:
    ficha["ctps"] = ctps
    ficha["contratação"] = join_year = int(input('Ano de contratação: '))
    ficha["salário"] = salary = int(input('Salário: R$ '))
    ficha["aposentadoria"] = 35 - (year - join_year) + age


print("-"*30)
for k, v in ficha.items():
    print(f"{k.title():<14} {v}")
