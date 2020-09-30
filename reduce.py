"""
Reduce não é uma funcao integrada buit in agora precisamos importar a partir do modulo functools
"""
from functools import reduce

numbers = 1, 2, 3, 4, 5, 6, 7, 8, 9
# Pega o valor da primeira interacao e armzaena numa variavel, e passa como parametro para a outra interacao
result = reduce(lambda x, y: x + y, numbers)
print(numbers)
print(result)
