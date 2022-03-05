"""
Exercicio 96

Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.
"""

def área(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura:.1f}x{comprimento:.1f} é de {a:.1f}m².')

área(float(input('Qual a largura do terreno? ')), float(input('Qual o comprimento do terreno? ')))
