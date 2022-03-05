"""
Exercício 98

Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo
e realize a contagem.

Seu programa tem que realizar três contagens através da função criada:

a) De 1 até 10. de 1 em 1
b) De 10 até 0. de 2 em 2
c) uma contagem personalizada.
"""


def contagem(início, fim, passo):
    print('~'*40)
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo *= -1
    print(f'Contagem de {início} até {fim} de {passo} em {passo}')
    if fim < início:
        passo *= -1
        fim -= 1
    for c in range(início, fim, passo):
        print(c, end=' ')
    print('FIM!')


contagem(1, 10, 1)
contagem(10, 0, 2)
contagem(
    int(input('Início: ')),
    int(input('Fim: ')),
    int(input('Passo: ')),
)
