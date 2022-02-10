# Recebe o sexo se F ou M
sexo = str(input('Qual o seu sexo? [F/M]: ')).strip()
while sexo not in 'MmFf':
    sexo = str(input('Opção invalida.\nQual o seu sexo? [F/M]: ')).strip()
if sexo in 'Ff':
    sexo = 'FEMININO'
else:
    sexo = "MASCULINO"
print('\nVocê informou ser do sexo {}.'.format(sexo))
