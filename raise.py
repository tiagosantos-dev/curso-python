"""
Disparando o propio erro com raise
raise - lanca exceções
OBS: raise é uma palavra reservada, não uma funcao
    ex:
    raise TipoDoError("Mensage do error")


"""

#O raise joga a execeção e sai do bloco
def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError("Texto precisa ser uma string")
    elif type(cor) is not str:
        raise TypeError("Cor precisa ser uma string")


# colore("fsdf", 1)
# colore("fsdf", 1)


