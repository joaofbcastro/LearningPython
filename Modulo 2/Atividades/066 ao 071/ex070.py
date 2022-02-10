totalmil = total = cont = 0
while True:
    produto = str(input('Informe o nome do produto>: ')).strip().capitalize()
    preço = float(input('Preço: R$'))
    # Soma o preço ao total.
    total += preço
    # Verifica se é a primeira ocorrência ou o preço é menor que o menor.
    cont += 1 
    if cont == 1 or preço < menor:
        barato = produto
        menor = preço
    # Se o preço for maior que mil, conte.
    if preço > 1000:
        totalmil += 1 
    # Verifica se a resposta está dentre as opções.
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    # Se a resposta for não, sair do loop.
    if resp == 'N':
        break
# Finalizando o programa.
print('{:-^40}'.format('Fim do programa!'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totalmil} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {barato} que custou R${menor:.2f}')
