palavrinhas = (
    'Aprender', 'Programar', 'Curso', 'Python', 'Gratis', 'Estudar', 'Mercado', 'Programador'
)
for palavra in palavrinhas:
    vogais = ''
    for l in palavra:
        if l.lower() in "a e i o u":
            vogais += l.lower()+' '
    print(f'Na palavra {palavra:<11} temos {vogais}')
