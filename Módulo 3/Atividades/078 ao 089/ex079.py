lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print('\033[32mValor adicionado com sucesso!\033[m')
    else:
        print('\033[31mValor duplicado! Não posso adicionar.\033[m')
    sair = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if sair in 'N':
        break
print('='*40)
print(f'Você adicionou os valores: {sorted(lista)}\n')
