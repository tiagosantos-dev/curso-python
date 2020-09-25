"""
DICTIONARY COMPREHENSION

SINTAXE
{chave:valor for valor ib iteravel}
"""

dict_numbers = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

#MULTIPLICA O VALOR POR ELE MESMO
novo_dict = {chave: valor * valor for chave, valor in dict_numbers.items()}
print(dict_numbers)
print(novo_dict)

list_numbers = [2, 3, 3, 4, 543, 343, 3423, 232, 232, 25, 34, 5, 56, 4534, 654, 56, 54]

novo_dict_numbers = {elemento_lista: elemento_lista / 5 for elemento_lista in list_numbers}

print(novo_dict_numbers)


nome = ['Tiago', "Joao", "Lucas", "Nayla", "Pedro", "Zilma", "Ayla"]
idade = [22, 20, 23, 38, 2, 64, 41]

agrupamento = {nome[i]: idade[i] for i in range(0, len(idade))}
print(agrupamento)

#NUMEROS PARES OU IMPARES
res = {elemento: ("par" if elemento % 2 == 0 else "impar") for elemento in list_numbers}
print(res)
