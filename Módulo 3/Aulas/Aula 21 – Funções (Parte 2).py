def contador(i, p, f):
    """
    Faz uma contagem e mostra na tela

    Parameters
    ----------
    i: Início da contagem
    p: Passo da contagem
    f: Fim da contagem
    """
    c = i
    while c <= f:
        print(f"{c} ", end="")
        c += p
    print("FIM!")

help(contador)