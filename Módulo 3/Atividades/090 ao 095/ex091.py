from random import randint
from time import sleep
from operator import itemgetter
# Módulo para ordenar items de um dicionário.

jogo = {
    "jogador1": randint(1, 6),
    "jogador2": randint(1, 6),
    "jogador3": randint(1, 6),
    "jogador4": randint(1, 6)
}

ranking = {}

print("JOGUEM OS DADOS")

for k, v in jogo.items():
    print(f"{k} tirou {v} no dado.")
    sleep(0.5)

print("--"*30, "\nRANKING DOS JOGADORES")
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for p, j in enumerate(ranking):
    print(f"{p+1}º lugar {j[0]} com {j[1]} pontos.")
    sleep(0.5)
