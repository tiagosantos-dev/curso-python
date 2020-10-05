#import random -> Dessa forma vc importa todo o modulo e todo o pacote
from random import random, uniform, choice, randint, shuffle

#metodo rando gera um numero aleatorio de 0 a 1
print(random())

#metodo uniforme gera numero de n a n , sendo eles pontos flutuante
print(uniform(0, 101))


for i in range(10):
    print(uniform(1, 101), end=", ")

print("\n")
for i in range(10):
    #metodo randint gera numero de n a n , sendo eles numeros inteiros
    print(randint(1, 100), end=", ")

print("\n")
#metodo choice retorna um elemento de um iteravel
frutas = ["Lucas", "Tiago", "Joao", "Pedro"]

print(choice(frutas))

#Metodo shuffre serve para embaralhar um iteravel
baralho = ["A", 10, 8, "K", 2, 7, 4, 3, 9, 6, 0, "J", 1, 5]

print(baralho)
shuffle(baralho)
print(baralho)
