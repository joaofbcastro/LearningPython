# Exibe o fatorial de um número

def fatorial(n: int, show: bool = False):
    """--> Calcula o fatorial de um número.

    Parameters
    ----------
    n: O número a ser calculado.
    show: (Opcional) Mostra ou não a soma.

    Returns
    -------
    O valor de Fatorial de um numero n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            print(' x ', end='') if c > 1 else print(' = ', end='')
        f *= c
    print(f)
    return f


fatorial(5, True)
