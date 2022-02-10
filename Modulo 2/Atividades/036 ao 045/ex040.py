print('')
nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
média = (nota1 + nota2) / 2
print('')
print('Sua média foi {:.1f}'.format(média))
if média < 5:
    print('Você está REPROVADO.')
elif 5 <= média < 7:
    print('Você está de RECUPERAÇÃO.')
elif média >= 7:
    print('Você foi APROVADO.')
print('')
