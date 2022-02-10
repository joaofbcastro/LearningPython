altura = float(input('Qual a sua altura em metros? '))
peso = float(input('Qual o seu peso atual em Kg? '))
imc = peso / (altura ** 2)
print('')
if imc < 18.5:
    status = 'Abaixo do Peso'
elif imc <= 25:
    status = 'Peso Ideal'
elif imc <= 30:
    status = 'Sobrepeso'
elif imc <= 40:
    status = 'Obesidade'
elif imc >= 40:
    status = 'Obesidade mórbida'
print('O seu IMC é de {:.1f}. Seu status é {}.'.format(imc, status))
