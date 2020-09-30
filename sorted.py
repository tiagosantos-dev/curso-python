"""
Sorted : pode ser usado por qualquer iteravel, serve para ordenar
OBS: é diferente da funcao sort() pois, so existe em list
"""

#Exemplo
from collections import deque

list_numeros = deque(range(11), maxlen=10)
print(f"utilizando o deque : {list_numeros}")
list_des = [3, 3, 32, 5, 1, 22, 2.2, 3, 1.2, 1.2, 0.5, 0.1, 0]
print(sorted(list_des))
print(f" Retorna uma lista: {type(sorted(list_numeros))}")
map_numbers = {elemento for elemento in range(21)}
print(map_numbers)
print(f"Retorna uma lista: {sorted(map_numbers)}")

tupla = tuple(range(31))
print(tupla)
#Ordena do maior para menor
print(sorted(tupla, reverse=True))


users = [
    {"username": "Pedro", "posts": ["Eu adoro pizzas", "Os fins nao justificam porra alguma"]},
    {"username": "Luana", "posts": []},
    {"username": "Joao", "posts": ["Flutter é melhor qe react native", "Dart é a linguagem de programacao top s2s2"]},
    {"username": "Lucas", "posts": ["O verdinho do cera da jamaica", "3mil em um dia"]},
    {"username": "Ayla", "posts": []},
    {"username": "Tiago", "posts": ["Prefiro cerveja haineken", "Brasil é o pais do futebol e da sacanagem"]},
    {"username": "JB", "posts": []},
    {"username": "Nayla", "posts": ["o Chocolate da cacau show e bom", "Amor de pai nunca tive"]},
    {"username": "Zilma", "posts": []}
]

print(users)
#ORDENANDO POR USERNAME DE ORDEM ALFABETICA
print(sorted(users, key=lambda x: x["username"]))

#ORDENANDO POR QUANTIDADE DE POST CRESCENTE
print(sorted(users, key=lambda x: len(x["posts"]), reverse=False))

