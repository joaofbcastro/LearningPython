nome = str(input('Digite o seu nome: ')).strip().title()
print('Muito prazer em te conhecer! \nSeu primeiro nome é {}.'.format(nome.split()[0]))
print('Seu ultimo nome é {}'.format(nome.split()[len(nome.split())-1]))
