#Tuplas São imutaveis, diferentes de Listas;
#Tuplas são recomendaveis para guardar dados estaticos

#DUAS FORMAS DE CRIAR UMA TUPLA : COM OU SEM PARENTESES



#TUPLA COM PARENTESES
meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro","Novembro", "Dezembro")

#TUPLA SEM PARENTESES
listaA = 1,2,3
print(type(listaA))

#TUPLA COM 1 ELEMENTO NÃO É TUPLA
#TUPLAS SAO DEFINIDAS POR VIRGULAS
tupla3 = (1) #RETORNA UM INT
print(type(tupla3))

tupla4 = (1,) #AGORA RETORNA UMA TUPLA, DEVIDO A VIRGULA
print(type(tupla4))

# print(len(listaA))
# print(min(listaA))
# print(sum(listaA))
# print(max(listaA))


#DESENPACOTANDO DADOS
# GERA UM VALUEERROR SE ESTIVER MAIS DADOS E MENOS VARIAVEL E VIRSA E VERCA..
valores = ("Tiago", "Santos")
nome, sobrenome = valores
print(nome,sobrenome)


# TUPLAS SAO IMUTAVEIS POREM PODEMOS, JUNTAR OUTROS ELEMENTOS
tupla1 = (1,2,3,4,5)
tupla2 =(6,7,8,9)
result = tupla1 + tupla2
print(result)

#RETORNA TRUE OU FALSE: SE HÁ O ELEMENTO 2 NA TUPLA
print(2 in tupla1)

#ITERANDO SOBRE UMA TUPLA
for elemento in result:
    print(elemento ,"Deu merda")

#SABER A POSICAO DE UM ELEMENTO EXPECIFICO
print(result.index(2))


#CLONANDO UMA TUPLAS

tuplaantiga = (1,2,3)
tuplanova = tupla2 #NA TUPLA NAO TEMOS O PROBLEMA SHELOW COPY
