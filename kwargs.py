"""
Este é um parametro, mas diferente do args que coloca os valores extras em uma tupla.  o kwargs
exige um parametros nomeados, e transforma esses parametros em dicionario
"""


def cores(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f" A COR FAVORITA DO(A) {pessoa.title()} É {cor}")


lista_nomes = ["TIAGO", "JOAO", "LUCAS", "PEDRO", "NAYLA"]
valores_cores = {}.fromkeys(lista_nomes, "PRETO")

cores(**valores_cores)
cores(tiago="verde", joao="azul", lucas="amarelo")
