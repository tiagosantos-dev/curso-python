"""
Generators tem a mesma funcao do comprehension porem com tuplas
generators é mais perfomatico que comprehension, pois a qnt de byte é menor.
"""
#Funcao getsizeof retorna quantidade de byte ocupado em memeoria
from sys import getsizeof
list_names = ["Carlos", "Cassandra", "Caliel", "Cibelle", "Cerveja"]
result = (elemento[0] == 'C' for elemento in list_names)
print(all(result))


list_comp = getsizeof([elemento * 10 for elemento in range(1000)])
set_comp = getsizeof({elemento * 10 for elemento in range(1000)})
dict_comp = getsizeof({elemento: elemento * 10 for elemento in range(1000)})
generators = getsizeof((elemento * 10 for elemento in range(1000)))


print(f"List Comprehension: {list_comp} bytes")
print(f"Set Comprehension: {set_comp} bytes")
print(f"Dict Comprehension: {dict_comp} bytes")
print(f"Generators Expression: {generators} bytes")

print(help(getsizeof))

#Retorna um Generators Object
print(f"Retorna :", type((elemento * 10 for elemento in range(1000))))
