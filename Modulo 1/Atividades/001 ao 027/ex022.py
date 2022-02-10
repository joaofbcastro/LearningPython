nome = str(input('Qual o seu nome completo? '.strip()))
print('-' * 36)
print('O nome completamente em maiusculo é {}.'.format(nome.upper()))
print('O nome completamente em minusculo é {}.'.format(nome.lower()))
print('O número total de letras sem espaçoes é {}.'.format(len(nome) - (nome.count(' '))))

print('O primeiro nome contém: {} letras.'.format(len(nome.split()[0])))
# Ou
print('O seu primeiro nome tem {} letras.'.format(nome.find(' ')))

print('-' * 36)
