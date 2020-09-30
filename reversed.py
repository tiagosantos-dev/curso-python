"""
RESERVED  - Serve para Inverter qualquer iteravel
OBS: Não confundi com a funcao reverse() , pois so existe em listas
"""

numbers = list(range(11))

print(list(reversed(numbers)))

#RETORNA UM list_reverseiterator
print(type(reversed(numbers)))

for letra in reversed("Tiago Santos"):
    print(letra, end="")


