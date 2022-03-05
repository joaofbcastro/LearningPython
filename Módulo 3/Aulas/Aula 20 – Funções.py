# Aula de funções

"""
Nessa aula foi apresentado o recurso sde função no python
com ele é possível fazer rotinas repetitivas com um simples comando.
"""

# Nesse exemplo a função escreverá na tela uma linha do tamanho desejado
def linha(tamanho: int):
    print('-'*tamanho)


linha(100)


# Nós também podemos colocar funções dentro de outras funções
def title(title: str):
    linha(len(title))
    print(title)
    linha(len(title))


title("Começou um novo ano!")
