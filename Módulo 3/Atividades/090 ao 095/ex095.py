# Esse código fa´ra perguntas de quem são os jogadores que fazem parte do time
# Após isso será feito o tratamento dos dados para serem exibidos na tela
# Nesse código contém uma validação de input.

time = []
while True:
    # Pergunta os dados do jogador.
    jogador = {"nome": str(input("Nome: ")), "partidas": []}
    for c in range(int(input("Quantas partidas jogou? "))):
        gols = int(input(f"Quantos gols na {c+1}ª partida? "))
        jogador['partidas'].append(gols)
    jogador['total'] = sum(jogador['partidas'])
    time.append(jogador)

    # Pergunta se quer continuar.
    while True:
        resp = str(input("\033[35mContinuar?\033[m [S/N] ")).upper()[0]
        if resp in "SN":
            break
        print("\033[31m[Error]\033[m Por favor informe uma resposta válida.")
    if resp == "N":
        break

# Mostrando os dados.

print(f"\n{'ID':<5}{'Nome':<15}{'Gols':<15}{'Total':<5}")
print('--'*20)
for id, p in enumerate(time):
    print(f"{id:<5}{p['nome']:<15}{str(p['partidas']):<15}{p['total']:<5}")

while True:
    while True:
        print('--'*20)
        id = int(input("Informe o ID do jogador: "))
        if id < len(time) or id == 999:
            break
        print("\033[31m[Error]\033[m Por favor informe uma resposta válida.")
    if id == 999:
        break

    print('--'*20)
    print(f"==  Partidas de \033[34m{time[id]['nome']:<4}\033[m  ==")
    for p, gols in enumerate(time[id]['partidas']):
        print(f"  No {p+1}º jogo fez {gols} gols")

print(f"\033[31m{'<= Encerrando =>':^40}\033[m")
