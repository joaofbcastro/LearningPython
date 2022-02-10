média = 0
homem_mais_velho = ''
velho_idade = 0
mulher_jovem = 0

for c in range(4):
    print(f'\nPessoa {c+1}\n----------------------------')
    nome = str(input('Qual é o seu nome?      '))
    idade = int(input('Quantos anos você tem?: '))
    sexo = int(input('Qual o seu sexo?\n[1] Masculino\n[2] Feminino\nDigite sua opção: '))
    print('----------------------------')
    média += idade
    if sexo == 1 and idade > velho_idade:
        homem_mais_velho = nome
        velho_idade = idade
    if sexo == 2 and idade <= 20:
        mulher_jovem += 1
média = média / 4
print('\n', '-=' * 20)

print('A média de idade do grupo é {} anos.'.format(int(média)))
if homem_mais_velho != '':
    print('{} é o homem mais velho do grupo, com {} anos.'.format(
        homem_mais_velho, velho_idade))
else:
    print('Não há homens nesse grupo')

if mulher_jovem != 0:
    print("Nesse grupo tem {} mulheres com menos de 20 anos.".format(mulher_jovem))
else:
    print('Não há mulheres com menos de 20 anos nesse grupo.')

print('', '-=' * 20)
