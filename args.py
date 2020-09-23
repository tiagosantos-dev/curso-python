"""
o args é um parametro com qualquer outro, isso significa que vc podera chamar qualquer
coisa, desde que comece com asterisco
"""


def somar_tudo(*args):
    # RETORNA UMA TUPLA
    return sum(args)


print(somar_tudo(3, 3, 3, 3))


lista_numeros = [2, 2, 2, 2, 43, 4, 4, 4, 4, 4]
tupla_numeros = (2, 2, 2, 2, 43, 4, 4, 4, 4, 4)

#o desempacotador é o asterisco
# por de baixo dos panos
# cria  uma variavel para cada elemento da lista
print(somar_tudo(*lista_numeros))
print(somar_tudo(*tupla_numeros))
