"""
UTILIZANDO LAMBDAS
CONHECIDAS POR EXPRESSOES LAMBDAS, SAO FUNCOES SEM NOME, OU SEJA FUNCAO ANONIMAS
"""


#FUNCAO EM PYTHON
def funcao(x): 
    return 3 * x + 1


#FUNCAO LAMBDA
var = lambda x: 3 * x + 1


# E COMO UTILIZAR EXPRESSOES LAMBDAS ?
calc = lambda x: 3 * x + 1

print(calc(3))


#DIVERSOS PARAMETROS
#FUNCAO STRIP : REMOVE ESPAÇAMENTO NO INCIO E NO FINAL DA STRING
nome_completo = lambda nome, sobrenome: nome.strip().title() + " " + sobrenome.strip().title()
print(nome_completo("    TIAGO    ", "   santos "))

#LAMBAS SEM PARAMETROS
res = lambda: "Como não amar python?"

print(res())

#OBS: SE PASSARMOS PARAMETROS A MAIS, ISSO CAUSARÁ UM TYPEERROR


lista_nomes = ["Silva Junior", "Santos Lucaas", "Santos Tiago", "Araujo de Silva Petter Alessa Luana"]


lista_nomes.sort(key=lambda sobrenome: sobrenome.split(" ")[-1].lower())
print(lista_nomes)


#FUNCAO QUADRATICA
# f(x) = a * x ** 2 + b * x + c


def funcao_quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


f = funcao_quadratica(5, 5, 5)

print(f(23))
