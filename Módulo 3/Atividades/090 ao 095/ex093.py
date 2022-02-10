jogador = {
    'nome': str(input("Nome: ")),
    'partidas': [],
    'total': None
}
for c in range(int(input(f'Quantas partidas {jogador["nome"]} jogou? '))):
    jogador['partidas'].append(
        int(input(f" Quantos gols {jogador['nome']} fez na {c+1}ª partida? ")))
jogador['total'] = sum(jogador['partidas'])

# Mostrando os dados na tela.

print("--"*30)
print(jogador)
print("--"*30)
for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}.")
print("--"*30)
print(
    f"O jogador {jogador['nome']} jogou {len(jogador['partidas'])} partidas.")
for p, i in enumerate(jogador['partidas']):
    print(f"  Na {p+1}ª partida fez {i} gols.")
print(f"Totalizando {jogador['total']} gols.")
print("--"*30)
