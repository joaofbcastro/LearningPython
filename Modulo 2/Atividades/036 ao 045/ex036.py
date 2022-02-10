# Emprestimo bancario
from asyncio import sleep

print('-.-'*15)
print('Bem vindo ao Simulador de Emprestimo')
print('-.-'*15)
casa = float(input('Quanto custa a casa que você quer comprar? R$'))
salário = float(input('Quanto é o seu salário? R$'))
anos = int(input('Em quantos anos você pretende pagar? '))
mensalidade = casa / (12 * anos)
print('')
print('Para financiar essa casa em {} anos você precisará pagar R${:.2f} por mês ao banco.'.format(
    anos, mensalidade))
print('')
print('30% de seu salário é R${}:'.format(int(salário * 0.30)))
if mensalidade <= (salário * 0.30):
    print('Por isso o seu mprestimo foi aprovado.')
else:
    print('Por isso o seu mprestimo foi negado.')
print('')
