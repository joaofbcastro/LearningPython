"""
Exercicio 97

Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como 
parâmetro e mostre uma mensagem com tamanho adaptável.

Ex: 
escreva('Olá mundo!')

Saida: 
~~~~~~~~~~
Olá mundo!
~~~~~~~~~~
"""


def escreva(mensagem: str):
    print('~'*len(mensagem))
    print(mensagem)
    print('~'*len(mensagem))


escreva(str(input('Escreva uma mensagem: ')))
