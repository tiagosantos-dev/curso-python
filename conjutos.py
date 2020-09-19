"""
CONJUNTOS SÃO BASEADOS EM CONJUNTOS DA MATEMATICA.
NAO POSSUI ELEMENTO DUPLICADOS
NAO SAO INDEXADOS
NAO SAO ORDERNADOS
SAO CHAMADOS TAMBEM DE SET
SAO REFERENCIADO COM AS CHAVES {}
    - UM DICIONARIO POSSUI, CHAVE E VALOR {1:"ARROZ"}
    - UM CONJUNTO SO POSSUI VALOR {"arroz","feijao"}

"""

#SE PASSAR UM VALOR EXISTENTE, ELE O IGNORA
conj = {"br", "fort", "sei", "la", "to", "nem", "veno", 2, 3}

print(type(conj))
print(conj)



for valor in conj:
    print(valor)


#COJUNTOS NAO SAO ORDENADOS
conj1 = {1,2,2,3,4,4,5,4,33,23,23,3,23,3,23,3,323,23,23}

print(conj1.add(3423432423423423423423))
print(conj1)


#SE TENTAR REMOVER UM ELEMENTO INEXISTENTE
#OCORRERÁ UM ERRO KEYERROR
print(conj1.remove(2)) #REMOVE PELO VALOR
conj1.discard(22222) #REMOVE O VALOR E SE NAO EXISTE NAO GERA ERRORP
print(conj1.discard(22222) )



#SHELLOW COPY E DEEP COPY

#SHELLOW
conjshellow =  conj
print(conjshellow)
conjshellow.add("vai replicar para os dois pois faz referencia e nao copiando")
print(conjshellow)
print(conj)
conjshellow.remove("vai replicar para os dois pois faz referencia e nao copiando")

#DEEP COPY
conjdeep = conj.copy()
conjdeep.add("nao vai replicar nao faz referencia")
print(conjdeep)
print(conj)



#ESCOLA DESAFIO

estudantes_java ={"Patricia","Leticia","Angel","Guilherme", "Tiago", "Marcos","Ana", "Vitoria"}

estudantes_python ={"sabrina","Tiago","Matheus","samantha", "Oliver", "DANIEL","Flavia", "Vitoria"}


#SABER TODOS OS OS NOMES DOS ALUNOS NOS DOIS CURSO
# 1 Forma de uniao
uniao1 = estudantes_java.union(estudantes_python)
print(uniao1) #REMOVE NOMES DUPLICADOS E FAZ UM NOVO SET

# 2 Forma de uniao
uniao2 = estudantes_python | estudantes_java #USANDO O PIPE SIGNIFICA A MESMA COISA DE UNION
print(uniao2)

#QUAIS ALUNOS ESTAO MATRICULADOS NOS DOIS CURSOS

#FORMA 1
intercecao = estudantes_java.intersection(estudantes_python) # PEGA O ELEMENTO QUE APARECER NAS DUAS SETS
print(intercecao)

#FORMA 1
intercecao2 = estudantes_java & estudantes_python # FAZ A MESMA COISA DA FUNCAO INTERSECTION
print(intercecao2)


#REMOVENDO ALUNOS QUE FAZEM OS DOIS CURSOS

so_python = estudantes_python.difference(estudantes_java)
print(so_python)
so_java = estudantes_java.difference(estudantes_python)
print(so_java)