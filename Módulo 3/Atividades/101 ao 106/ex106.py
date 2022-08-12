from time import sleep


def show(text):
    print('\033[0;30;45m' + ('~' * len(text)))
    print(text)
    print(('~' * len(text)) + '\033[0m')


def main():
    while True:
        q = input('\nFunção ou Biblioteca > ')
        if q.lower() == 'sair':
            break
        show('Buscando ajuda...')
        sleep(2)
        help(q)


main()
