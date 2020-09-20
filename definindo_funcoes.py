"""
DEFINICAO DE FUNCAO
def nome_da_funcao(parametros_entrada):
    bloco de codigo a ser executado quando chamar a funcao
"""
#EXEMPLO DE ULITIZACAO DE FUNCOES
cores = ["red", "blue", "grey", "yellow", "green", "pink", "white", "black"]


def pegando_cores(lista, dassda):
    for element in dassda:
        print(f"COR : {lista[element]}, ID : {element}")


asas = [0, 1, 2, 3, 4, 5, 6, 7]

pegando_cores(cores, asas)

#VARIAVEIS PODEM RECEBER FUNCOES
#OBS : NAO DEVE USAR PARENTESE SE FOR REFERENCIAR A UMA VARIAVEL
alternando_a_funcao = pegando_cores
alternando_a_funcao(cores, asas)


