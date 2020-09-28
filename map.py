"""
MAP : COMO MAP FAZEMOS MAPEAMENTO DE VALORES PARA FUNCAO
MAP RETORNA UM MAP OBJECT
RECEBE DOIS PARAMENTROS : UMA FUNCAO E UM ITERAVEL.
"""
import math


def area(r):
    """Função retorna a area total de um circulo"""
    return math.pi * (r ** 2)


print(area(2))

lista_raios = [12, 24, 5, 2.5, 6, 3, 4, 1.5, 7, 9]


# FORMA COMUM DE FAZER UMA ITERACAO SOBRE UMA COLLECTION
result_raios = []
for elemento in lista_raios:
    result_raios.append(round(area(elemento), 2))


print(result_raios)

#UTILIZANDO  MAPP
result_raios_map = map(area, lista_raios)
print([round(elemento, 2) for elemento in result_raios_map])

#UTILIZANDO EXPRESSOES MAP + LAMBDA
result_raios_lbd = map(lambda r: math.pi * (r ** 2), lista_raios)
print([round(elemento, 2) for elemento in result_raios_lbd])


#CONVERTENDO DE GRAUS CELSIUS PARA FAHRENHEIT
#FORMULA (C x 9/5) + 32
lista_estados = [("CEARA", 32), ("SAO PAULO", 17), ("RIO DE JANEIRO", 22), ("PARAIBA", 35), ("BAHIA", 28),
                 ("PARA", 32), ("TOCANTIS", 23), ("SERGIPE", 22)]
celsius_para_fahrenheit = lambda c: (c[0], (c[1] * (9/5)) + 32)

result_estados_convertido = map(celsius_para_fahrenheit, lista_estados)
print(list(result_estados_convertido))



