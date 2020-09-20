from random import random
from math import floor


def pega_numero_aleatorio():
    valor = floor(random() * 100 % 2)
    return valor


def jogo_moeda():
    if pega_numero_aleatorio() > 0:
        return 'CARA'
    else:
        return'COROA'


print(jogo_moeda())



