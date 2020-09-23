"""
Documentando funcoes com Docstring

"""

#EXMPLOS

def diz_oi():
    """ Uma Função simples que retorna um oi"""
    print("Oi")


print(diz_oi())
print(diz_oi.__doc__)
print(help(diz_oi))


def calcular(valor, valor2):
    """
    :param valor: Primeiro valor a ser somado
    :param valor2: Segundo valor a ser somado
    :return: Retorna a soma dos dos dois valores
    """
    return valor + valor2
