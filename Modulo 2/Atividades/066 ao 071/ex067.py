while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*38)
    if valor < 0:
        print('Programa de tabuada encerrado! VOLTE SEMPRE\n')
        break
    for c in range(1, 11):
        print(f'{valor} x {c:<2} = {valor*c}')
    print('-'*38)
