# Manipulando texto

# Fatiamento
frase = 'Curso em Video Python'
print(frase[9])         # Mostra o caracter da casa 9
print(frase[9:13])      # Mostra os caracteres do 9 aoo 12 pq o 13 n conta
print(frase[9:21:2])    # Mostra os caracteres do 9 ao 21 pulando de 2 em 2
print(frase[:5])        # Mostra os caracteres do inicio até o 4.
print(frase[15:])       # Mostra os caracteres do 15 até o final.
print(frase[9::3])      # Mostra os caracteres do 9 até o final pulando de 3

print('')

# Analise
# Mostra o compimento da Variavel.
print(len(frase))

# Mostra quantas vezes aparece a letra "o"
print(frase.count('o'))

# Mostra quantas vezes aparece a letra "o" até o caracter 12
print(frase.count('o', 0, 13))

# Mostra em qual posisão começa a frase "deo"
print(frase.find('deo'))

# Quando não existe a frase ele retorna o valor -1
print(frase.find('Android'))

# Retorna um valor boleano para a existencia da frase
print('Curso' in frase)

print('')

# Transformação
# Substitui temporariamente um atributo por outro
print(frase.replace('Python', 'Android'))

# Mostra todas as letras em Maiusculo
print(frase.upper())

# Mostra todas as letras em minusculo
print(frase.lower())

# Mostra a primeira letra em maiusculo e as demais em minusculo
print(frase.capitalize())

# Mostra as primeiras letras em maiusculo e as demais em minusculo
print(frase.title())

frase = '   Aprenda Python  '

# Remove os espaços inuteis nas laterais
print(frase.strip())        # r ou l para escolher o lado

frase = 'Curso em Video Python'

# Divisão
# Corta as palavras dentro da variavel
print(frase.split())

# Junção
# Junta as palavras com o caracter inserido nos espaços vazios.
print('-'.join(frase))
