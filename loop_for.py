#ESTRUTURA DE REPETICAO
"""
Metodo range() gera uma contagem de numeros, recebe como primeiro parametro o valor inicial
o segundo paramentro ate onde deseja contar
"""
nome ="Tiago Santos"

lista = [1, 2,34,4, "Tiago", "Seila", "qualquer coisa"]

for letra in nome: #Itereando sobre uma string
    print(letra)

for numero in range(100):  #iterando sobre um range
    print(numero)

for elementoDalista in lista: #iterando sobre um array
    print(elementoDalista)


for cadaLetra in enumerate(nome): #iterando sobre cada char de uma string, retorna tambem a posicao
    print(cadaLetra[0]) #retorna o identficador de cada letra
    print(cadaLetra)


valorInciall = int(input("Digite aqui o valor Inicial:"))
valorFinall =int(input("Digite aqui o valor Final:"))
valorIncremento = int(input("Incrementar de quanto em quanto:"))
for valor in range(valorInciall, valorFinall, valorIncremento):
    print(valor)

qntfinal = int(input("Informe um numero:\n"))

for valor in range(1, qntfinal):
    print("\U0001F61C" * valor)

emoji ="0001F61C"
for n in range(1, qntfinal + 1):
    valorDivisivel = int(input(f"Digite um valor que será dividido por {n} :"))
    result = valorDivisivel / n
    print(f"Base divisora: {n}")
    print(f"numero Divisivel: {valorDivisivel}")
    print(f"TOTAL: {result}")



for valor in range(10 ,0 ,-1): # Decrementando de 10 a 0
    print(valor)








    #U+1F61C
    #U0001F61C
