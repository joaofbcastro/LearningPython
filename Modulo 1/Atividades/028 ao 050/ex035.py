s1 = float(input('digiete um segmento:   '))
s2 = float(input('Digite outro segmento: '))
s3 = float(input('Digite outro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Sim, é possivel formar um triangulo')
else:
    print('Não, não é possivel formar um triangulo')
