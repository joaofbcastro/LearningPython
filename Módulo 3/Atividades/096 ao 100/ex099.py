"""
Exercício 99 

Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores 
inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior 
"""

def maior(*valores):
    print('~'*40)
    print(f'Foram informados {len(valores)} valores')
    print(f'{valores}')
    print(f'O maior valor informado foi {max(valores)}')

maior(1,5,4,7,8,5,44,5,4,7,5,5,4,45,4,5,4,44,5)