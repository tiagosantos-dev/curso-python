
receita = {"jan": 120, "fev": 323, "marc": 342}
#iterar sobre um dicionario

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])


# Retorna um dicionario de chaves
print(receita.keys())

# Recomendado para ter acesso as chaves
# Retorna um dicionario de chaves
for chavee in receita.keys():
    print(chavee)


# Recomendado para ter acesso os valores
# Retorna um dicionario de valor
for valor in receita.values():
    print("valores ", valor)


# DESEMPACOTANDO  CHAVES E VALOR
for chave, valor in receita.items():
    print("valor",valor ," da chave",chave)


print(sum(receita.values()))
print(min(receita.values()))
print(max(receita.values()))
print(len(receita))