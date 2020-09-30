"""
zip() - Cria um iteravel (zip Object) que agrega elemento
de cada um dos dois iteraveis passando como entrada em pares
"""

list_letras = ["T", "L", "J"]
list_nomes = ["iago", "ucas", "oão"]

print(type(zip(list_letras, list_nomes)))
result = list(zip(list_letras, list_nomes, [1, 2, 3]))

#É UTILIZADO APENAS UMA VEZ, DEPOIS É APAGADO DA MEMORIA
print(result)

#UTILIZA COMO PARAMETRO O MENOR VALOR DE UM ITERAVEL
lista_um = [1, 2, 3]
lista_dois = [4, 5, 6]
lista_tres = [7, 8, 9, 10, 11, 12, 13, 14]

#SE A LISTA FOR MAIOR ELE DESCATA O RESTANTE DOS ELEMENTOS.
resultado = list(zip(lista_um, lista_dois, lista_tres))
print(resultado)


tupla = ("Tiago", 1, "seila", "alguma coisa")
dicionario = {"A": 22, "B": 33, "C": 44, "D": 55}
mapa = {1, 2, 3, 4, 5}

zipando = list(zip(tupla, dicionario.values(), mapa))
print(zipando)

nota_um = [1, 4, 10]
nota_dois = [5, 8, 3.9]
nota_tres = [5.5, 4.9, 2]

alunos = ["LUCAS", "TIAGO", "JOAO"]
#PEGANDO A MAIOR NOTA
resulta = {elemento[0]: max(elemento[1], elemento[2]) for elemento in zip(alunos, nota_um, nota_dois, nota_tres)}
print(resulta)
