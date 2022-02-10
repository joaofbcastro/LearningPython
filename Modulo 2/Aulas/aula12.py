print('')
nome = str(input('Qual é o seu nome? '))
print('')
if ('João' in nome) == True:
    print('Que nome lindo você tem, combina com seus olhos... Rs.')
elif nome == 'Marcos' or nome == 'Claudio' or nome == 'Maria':
    print('Seu nome é bem popular aqui no Brasil.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}.'.format(nome))
print('')
