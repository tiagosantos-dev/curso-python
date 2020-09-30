"""
Funcao min() - Retorna o menor valor de um iteravel
Funcao max() - Retorna o valor maior de um iterval
"""


numbers = [1, 2, 3, 3, 23, 232, 323, 523523, 46346345, 324324234]

print(f"Retornando o maior valor: {max(numbers)}")
print(f"Retornando o menor valor: {min(numbers)}")

#RETORNA UM INT
print(type(max(numbers)))

tupla = (1, 2, 3, 3, 23, 232, 323, 523523, 46346345, 324324234)
print(f"O maior numero da tupla: {max(tupla)}")

mapa = {1, 2, 3, 3, 23, 232, 323, 523523, 46346345, 324324234}
print(f"O maior numero da mapa: {max(mapa)}")

#RETORNA A CHAVE DO MAIOR
dicionario = {"A": 1, "B": 2, "C": 3, "D": 3, "E": 23, "F": 232, "G": 323, "H": 523523, "I": 46346345, "J": 324324234}
print(f"A chave com o maior numero da dicionario: {max(dicionario)}")

#UTILIZANDO VALUES RETORNA O MAIOR VALOR
dicionario = {"A": 1, "B": 2, "C": 3, "D": 3, "E": 23, "F": 232, "G": 323, "H": 523523, "I": 46346345, "J": 324324234}
print(f"O maior numero da dicionario: {max(dicionario.values())}")


