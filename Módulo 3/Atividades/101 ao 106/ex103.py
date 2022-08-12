# Mostra as informações de um jogador mesmo que as informações inseridas
# sejam invalidas.

def ficha(nome: str = "<Desconhecido>", gols: int = 0):
    print('--------------------------------')
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))

n = "<Desconhecido>" if n.strip() == '' else n
g = int(g) if g.isnumeric() else 0

ficha(n, g)
