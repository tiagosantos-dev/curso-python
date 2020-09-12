listaA = [1, 23, 5, 6, 2, 4]
listaB = ['t', 'i', 'a', 'g', 'o']



#ADICIONANDO ELEMENTO PROPIO DE UMA LISTA
listaB.extend(listaA)
print(listaB)

#ADICIONANDO UM VALOR NO ULTIMO ELEMENTO DA LISTA
print(listaA)
listaA.append(2)
listaA.append(listaB)
print(listaA)


#ORDENANDO TODOS OS ELEMENTOS DA LISTA DE A-Z 0-, se FOR SOMENTTE NUMERO OU SOMENTE LETRA
print(listaA)
#listaA.sort()
print(listaA)
print(dir(listaA))

#INSERINDO UM VALOR EM QUALQUER POSICAO
listaB.insert(2, 'id')
print(listaB)


#USANDO RANGE PARA CRIAR LISTA DE NUMEROS

listaC = list(range(10))
print(listaC)


#QUANTIDADE DE ELEMENTO DENTRO DE UMA LISTA

print(len(listaC))



#COPIANDO UMA LISTA

listaCOPY = listaA.copy()
print(listaCOPY)



#REMOVENDO O ULTIMO ELEMENTO DA LISTA
#RETORNA O ELEMENTO APAGADO
#PODE SER COLOCADO A POSICAO DE UM ELEMENTO PARA SER APAGADO

print(listaC)
elementoExcluido = listaC.pop()
print(elementoExcluido)
print(listaC)




#APAGANDO OS ELEMENTO DE UMA LISTA
print(listaCOPY)
listaCOPY.clear()
print(listaCOPY)



#STRING EM LISTA
nome = "Tiago Batista"
nome = nome.split(" ")

print(nome)


#TODOS OS CHAR EM UMA LISTA
nomeLista ="Tiago Santos Batista"
print(nomeLista.split())


cores = ["Branc", "Preto", "Azul", "Verde", "Laranja"]
#DO ULTIMO AO PRIMEIRO
print(cores[-1])
print(cores[-2])
print(cores[-3])
print(cores[-4])
print(cores[-5])
#print(cores[-6]) errro não existe posicao


numemros = [1, 2, 4, 6, 7, 8, 9, 0, 43, 1, 1]
print("Numero minimo dA LISTA :", min(numemros))
print("Numero maximo da lista", max(numemros))
print("Soma de todos os elementos da lista", sum(numemros))

#ITERANDO SOBRE UMA LISTA
for indice, cores in enumerate(cores):
    print(indice, cores)


#SABENDO QUAL POSICAO DO ELEMENTO NA LISTA
listaElemento = ["Playstation 1", "Playstation 2", "Playstation 3", "Playstation 4", "Playstation 5" ]
playEncontrado = listaElemento.index("Playstation 4")
print(playEncontrado)

#BUSCANDO UM INDEX A PARTIR DO ELEMENTO 3
print(listaC.index(7, 3))

print(listaC)

#PEGANDO ELEMENTO DE 0 A 3
print(listaC[0: 3])

#PEGANDO VALORES DE 2 EM 2
print(listaC[::2])

#INVERTENDO UMA LISTA DO ULTIMO AO PRIMEIRO
nome.reverse()
print(nome)
