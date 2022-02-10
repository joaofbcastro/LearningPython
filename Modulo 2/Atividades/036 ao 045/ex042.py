s1 = float(input('Digiete um segmento:   '))
s2 = float(input('Digite outro segmento: '))
s3 = float(input('Digite outro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    if s1 == s2 == s3:
        tipo = 'Equilatero'
    elif s1 != s2 != s3 != s1:
        tipo = 'Escaleno'
    else:
        tipo = 'Isórceles'
    print('\nSim, é possivel formar um triangulo do tipo {}.'.format(tipo))
else:
    print('Não, não é possivel formar um triangulo')
