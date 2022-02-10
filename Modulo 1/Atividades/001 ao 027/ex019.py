# Escolhe um aluno aleatorio
from  random import choice
aluno1 = str(input('Qual o nome do primeiro aluno? '))
aluno2 = str(input('E o nome do segundo? '))
aluno3 = str(input('E o nome do tercceiro? '))
aluno4 = str(input('E o nome do quarto aluno? '))
lista = [aluno1, aluno2, aluno3, aluno4]
print('O aluno escolhido foi: {}'.format(choice(lista)))
