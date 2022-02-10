from datetime import datetime

soma = 0
pessoas = []
while True:
    ficha = {"nome": str(input("Nome: ")).strip()}

    while True:
        ficha["sexo"] = str(input("Sexo [F/M]: ")).upper()[0]
        if ficha["sexo"] in "FM":
            break
        print("\033[31m[Error]\033[m Por favor informe F ou M.")

    ficha["idade"] = (datetime.now().year - int(input("Nascimento: ")))
    soma += ficha['idade']
    pessoas.append(ficha)

    while True:
        resp = str(input("\033[34mQuer continuar? [S/M] \033[m")).upper()[0]
        if resp in "SN":
            break
        print("\033[31m[Error]\033[m Por favor informe S ou N.")
    if resp == "N":
        break

# Mostrando os dados.

media = soma / len(pessoas)

print(f"[A] - Foram cadastradas {len(pessoas)} pessoas.")
print(f"[B] - A média de idade foi de {media:.0f} anos.")
print(f"[C] - Mulheres cadastradas: ", end="")
for p in pessoas:
    if p['sexo'] == "F":
        print(p['nome'], end=" ")
print(f"\n[D] - Pessoas com idade acima da média: ", end='')
for p in pessoas:
    if p['idade'] > media:
        print(f"{p['nome']} com {p['idade']} anos,", end=" ")
print()
