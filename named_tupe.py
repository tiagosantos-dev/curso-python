"""
NAMADE TUPE -> UMA TUPLA REFERECIADO DE UM NOME


"""
from collections import namedtuple

tupla = ("toto", 1, 2, 2, 2,)
print(tupla)

# 1 FORMA DE DECLARAR PARAMETRO
cachorro = namedtuple("cachorro", ["nome", "raca", "cor"])

# 2 FORMA DE DECLARAR PARAMETRO
cachorro2 = namedtuple("cachorro", "nome,raca,cor")

# 3 FORMA DE DECLARAR PARAMETRO
cachorro3 = namedtuple("cachorro", " nome raca cor")

toto = cachorro("toto", "labrador", "branca")
print(toto)
print(toto.cor)  #ACESSANDO PARAMETRO POR NOME
print(toto.raca)