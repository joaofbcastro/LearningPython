# Verifica se a frase inserida é um palíndromo
frase = ''.join(str(input('\nEscreva uma frase (sem acentos): ')).upper().strip().split())
inverso = frase[::-1]
if inverso == frase:
    resultado = "é um palíndromo"
else:
    resultado = 'não é um palíndromo'
print('A frase inserida {}.\n'.format(resultado))
