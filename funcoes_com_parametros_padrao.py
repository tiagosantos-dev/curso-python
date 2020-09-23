
def exponencial(numero, potencia=2):
    #Potencia por padrao recebe valor 2
    return numero ** potencia


print(exponencial(2, 2))
print(exponencial(2))

#CASO EXISTA APENA UM VALOR PADRAO ELE DEVE SER O ULTIMO A DECLARAR
#def teste(potencia=2, numero ):
#    return  numero ** potencia


def mostrar_informacoes(nome="Tiago", instrutor=False):
    if nome == "Tiago" and instrutor:
        return "Ola Instrutor !!"
    elif nome == "Tiago" and not instrutor:
        return "Pensei que fosse o Instrutor"
    else:
        return f"Olá {nome}"


print(mostrar_informacoes())
print(mostrar_informacoes(instrutor=True))
print(mostrar_informacoes("Fulano"))
print(mostrar_informacoes("Sicrano", True))


def somar(a,b):
    return a + b


def dividir(a, b):
    return a / b


def multiplicar(a, b):
    return a * b


def diminuir(a, b):
    return a - b


def calcular(valor, valor2, operacao=somar):
    return operacao(valor, valor2)


print("Calculando com funcao Padrao:", calcular(2, 2))
#SEM PARANTESES
print("Calculando com funcao Parametrizada:", calcular(2, 2, diminuir))
#SEM PARANTESES
print("Calculando com funcao Parametrizada:", calcular(2, 2, multiplicar))
#SEM PARANTESES
print("Calculando com funcao Parametrizada:", calcular(2, 2, dividir))

#PREFERENCIAS DE VARIAVEIS
valor = 0


def incrementar():
    global valor
    valor = valor + 1
    return valor


incrementar()
print(valor)


#UMA FUNCAO DENTRO DA OUTRA

def fora():
    incremento = 0

    def dentro():
        nonlocal incremento
        incremento = incremento + 1
        return incremento
    return dentro()


print(fora())
print(fora())
print(fora())


