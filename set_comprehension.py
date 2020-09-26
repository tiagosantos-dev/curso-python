"""
SET COMPREHENSION
 LEMBRANDO NAO ACEITA NUMEROS REPETIDOS !!

"""


numeros = {elemento for elemento in range(0, 11)}
print(numeros)
print(type(numeros))

#TRANSFORMANDO NUMEROS AO QUADRADO

numeros_ao_quadrado = {elemento ** 2 for elemento in numeros}
print(numeros_ao_quadrado)

#TRANSFORMANDO UM SET EM DICIONARIO COM VALORES AO QUADRADO E A CHAVE O PROPRIO ELEMENTO :D
dict_ao_quadrado = {elemento: elemento ** 2 for elemento in numeros}
print(dict_ao_quadrado)

#LETRAS
nome = "tiago santos batista"

set_letras_nome = {letra for letra in nome}
print(set_letras_nome)
