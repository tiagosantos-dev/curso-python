"""
LISTA ALINHADAS
"""

#MATRIZ 3X3

matriz_tres_por_tres = [["Linha1/coluna 1", "Linha1/coluna 2", "Linha1/coluna 3"],
                        ["Linha2/coluna 1", "Linha2/coluna 2", "Linha2/coluna 3"],
                        ["Linha3/coluna 1", "Linha3/coluna 2", "Linha3/coluna 3"]]

print(matriz_tres_por_tres)

#ACESSANDO LINHAS E COLUNAS
print("Acessando linha 1 coluna 3: ", matriz_tres_por_tres[0][2])
print("Acessando linha 2 coluna 2: ", matriz_tres_por_tres[1][1])

#ITERAÇOES
#LOOP COMUM
for lista in matriz_tres_por_tres:
    for elemento in lista:
        print(elemento)

#LIST COMPREHENSION
todos_elementos_matriz = [elemento for lista in matriz_tres_por_tres for elemento in lista]
print(todos_elementos_matriz)

#TABULEIRO DE 6X6
tabuleiro = [[elemento for lista in range(1, 7)] for elemento in range(1, 7)]
print(tabuleiro)
