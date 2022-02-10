num = int(input('Digie um número inteiro: '))
print('''
Escolha uma das opções:
[1] Converter para Binario.
[2] Converter para Octal
[3] Converter para hexadecimal
''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para Binário é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para Octal é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('A opção "{}" é invalida, por favor tente novamente.'.format(opção))
print('')
