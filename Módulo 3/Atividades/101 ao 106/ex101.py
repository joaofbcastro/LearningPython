# Crie uma função chamada votar() que recebe como parametro o ano de nascimento
# de uma pessoa e retorna um valor literal. (Negado, opcional, obrigadtório.)
from datetime import datetime


def votar(nasc: int) -> str:
    """
    Verifica se uma pessoa tem voto obrigatório, negado ou opcional.
    
    Parameters
    ----------
    nas: Ano de nascimento do individuo.
    
    Return
    ----------
    Retorna uma string contendo o valor literal
    """
    anoAtual = datetime.now().year
    idade = anoAtual - nasc
    if idade < 16:
        r = "NÃO VOTA"
    elif idade >= 18 and idade < 65:
        r = "VOTO OBRIGATÓRIO"
    else:
        r = "VOTO OPCIONAL"
    return f"Com {idade} anos: {r}."

print("------------=[#]=------------")
anoNasc = int(input("Em que ano você nasceu? "))
r = votar(anoNasc)
print(r)