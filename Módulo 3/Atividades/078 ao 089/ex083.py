valor = []
valor += str(input('Digite uma expressão: '))
print('Essa expressão é válida!' if valor.count('(') == valor.count(')') else 'Essa expressão não é válida!')
