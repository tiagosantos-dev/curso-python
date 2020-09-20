"""
Ordered dict -> GARANTE A ORDENACAO DOS ELEMENTOS

"""

from collections import OrderedDict

lista = ["id", "nome", "cpf", "telefone", "sexo"]

dicionario = OrderedDict().fromkeys(lista, None)

print(dicionario)

dictt1 = {"a":1 , "b":2}
dictt2 = {"b":2 , "a":1}
#RETORNA TRUE POIS A ORDER NAO IMPORTA EM DICIONARIOS
print(dictt1 == dictt2)

order_dict1 = OrderedDict(a=1, b=2)
order_dict2 = OrderedDict(a=2, b=1)

#RETORNA FALSE POIS A ORDEM IMPORTA
print(order_dict1 == order_dict2)