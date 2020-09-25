"""
LIST COMPREHENSION
- UTILIZAMOS PARA  NOS PODEMOS GERAR NOVAS LISTA COM DADOS PROCESSADOS A PARTIR DE OUTRO ITERAVEL.
#SINTAXE
[dado for int iteravel]
"""

numeros = [1, 2, 2, 3, 4, 4, 5, 6, 6]

#PRIMEIRO VEM A EXPRESSAO, DEPOIS O LOOP
#PARA CADA ELEMENTO DA LISTA DE NUMEROS
# MULTIPLIQUE POR 10 E ADICIONE NA VARIAVEL res.
res = [numero * 10 for numero in numeros]
print(res)

#DESFAIO MULTIPLICAR TODOS OS ELEMENTOS POR 100

#LOOP COMUN
lista_ao_cem = []
for elemento in numeros:
    lista_ao_cem.append(elemento * 100)

print(lista_ao_cem)

#LIST COMPREHENSION

lista_ao_cem_dois = [elemento * 100 for elemento in numeros]
print(lista_ao_cem_dois)

# EXEMPLO TITLE
lista_convidados = ["pedro", "ana", "isabela", "creuza", "italo", "silvinha", "raimundinho"]

lista_ordenada = [nome.title() for nome in lista_convidados]
print(lista_ordenada)

#TRANSFOMANDO TODOS OS ELEMENTOS EM STRING
lista_numbers = [34, 333, 3423, 33.3, 235, 0.5, 9.5, 129.4]
lista_string = [str(elemento) for elemento in lista_numbers]
print(lista_string)

#GERANDO UMA LISTA COM NUMEROS PARES
pares = [elemento for elemento in numeros if elemento % 2 == 0]
impares = [elemento for elemento in numeros if elemento % 2 == 1]
print(f"Numeros pares: {pares}")
print(f"Numeros impares: {impares}")

# pares = [elemento for elemento in numeros if not elemento]
# impares = [elemento for elemento in numeros if elemento]
# print(f"Numeros pares: {pares}")
# print(f"Numeros impares: {impares}")
