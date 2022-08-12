def leiaInt(text: str):
    while True:
        n = input(text)
        if n.isnumeric():
            n = int(n)
            break
        print('\033[0;31mERRO! Insira um número inteiro válido.\033[0m')
    return n


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')