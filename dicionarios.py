#EM OUTRAS LINGUAGEM DICIONARIO É CHAMADO DE MAPAS, COM CHAVE E VALOR

# 1 FORMA PARA CRIAR UM DICT
paises = {"BR": "Brasil", "EUA": "Estados Unidos", "PY": "Paraguai"}

# 2 FORMA PARA CRIAR UM DICT
paises2 = dict(du="dubai", nv="novaZelandia")

print(type(paises))

print("O valor comparado é igual a dict : ", type(paises) == dict)

#

#Acessar valor via chave 1FORMA
print(paises["BR"])
print(paises["EUA"])
print(paises2["du"])
print(paises2["nv"])
#KEYError valor nao encotrado
#print(paises["DU"])

#2 forma de acessar via chave (RECOMENDADO) 2FORMA
print(paises.get("EUA"))
print(paises.get("BR"))
print(paises2.get("du"))



#Podemos definir um valor padrao caso nao encontre a chave
pais = paises2.get("br", "Pais não encontrado")

print(f"o pais e {pais}")


#Verificar se determinada chave se encontra no dicionario
print("BR" in paises)
print("EUA" in paises)
print("USR" in paises)


localiade = {
    (3.7928829, 38.4955035) : "Casa do tiagooooo",
    (4.6628829, 44.4445035): "Casa da puta que pariu",
    (5.3488933, 23.2353432): "Casa"

}

print(localiade[(3.7928829, 38.4955035)])

print(type(localiade))

log = {"mai":344, "jun":654, "jul":543}

receita ={ "jan": 100, "fev": 333, "marc": 233}

#ADICIONANDO UM NOVO ELEMENTO NO DICT 1FORMA
#CASO JA TENHA UMA CHAVE, ELE ATUALIZAR O VALOR
receita["abril"]= 443
print(receita)

#ADICIONANDO UMNOVO ELEMENTO NOP DICT 2 FORMA
receita.update(log)
print(receita)

# 1 FORMA DE EXLCUIR (MAIS USADA)
#RETRONA O VALOR ESCLUIDO

retorno = receita.pop("jun")
print(retorno)

# 2 FORMA DE EXCLUIR (NÃO RETORNA NADA)
# SE A CHAVE NÃO EXISTIR HAVERÁ UM ERROR
del receita["jul"]
print(receita)


"""
DESAFIO:    CARRINHO
            -NOME
            -QUANTIDADE
            -PRECO
"""

# 1 FORMA USANDO DICIONARIOS (MAIS SEGURO)
carrinho = []

produto1 = {"nome":"Curso de Programacao Python", "quantidade":1, "preco":30.00}
produto2 = {"nome":"Machine learning", "quantidade":1, "preco":50.00}
produto3 = {"nome":"Data Scene", "quantidade":1, "preco":29.00}

carrinho.append(produto1)
carrinho.append(produto2)
carrinho.append(produto3)
print(carrinho)


#2 FORMA USANDO LISTAS (NAO RETORNA INDICE)

carrinho2 =[]

produto4 = ["Curso de java",1, 23.00]
produto5 = ["Curso javascript",1, 32.00]

carrinho2.append(produto4)
carrinho2.append(produto5)
print(carrinho2)


#3 FORMA USANDO TUPLAS



produto6 = ("OpenCV e Python", 1, 24.30)
produto7 = ("TensorFlow compelto",1 ,26.90)

carrinho3 = produto6, produto7
print(carrinho3)



#FROMKEYS (ADICIONA PARA CADA ELEMENTO O MESMO VALOR)
novo = {}.fromkeys(["nokme","quantidade","valor"], None)
print(novo)
print(type(novo))

#Para cada caractere o mesmo valor
novo2 = {}.fromkeys("DEU MERDA", None)
print(novo2)


#TIPO NONE

valor = None

print(type(valor) )
#SEMPRE SERÁ FALSE


#METODOS DICT

#COPIANDO UM DICT
dictatual = {"a":22, "b":233, "c":98}

# 1 FORMA
#SHELLOW COPY, ALTERA NAS DUAS LISTAS
dictnovo = dictatual
dictnovo["d"]= 300
print(dictatual)
print(dictnovo)

#2 FORMA
dictnovo = dictatual.copy()
dictnovo["e"] = 292
dictnovo.update({"f": 33})
print(dictatual)
print(dictnovo)

#METODO FROMKEYS RECEBE DOIS PARAMETROS 1 ITERAVEL E O OUTRO UM VALOR
dictiteravel = {}.fromkeys(["id","user","address","number",], "underfined")
print(dictiteravel)

dictnumbers = {}.fromkeys(range(11), "under")
print(dictnumbers)

#UTILIZANDO O KEYS
result = dictnumbers.keys() #É DIFERENTE DE LISTA
print("VALOR RETORNADO PELO METODO KEYS",result)
print(type(result))


# ITERANDO SOBRE UM DICT
for chave in dictnumbers.keys():
    print(dictnumbers[chave])

#UTILIZANDO METEDO VALUES : RETORNA  O VALOR
for valor in dictnumbers.values():
    print(valor)


#UTILIZANDO O METODO ITENS()
meses = {}.fromkeys(range(13 - 1), None)
mesesNome =["Jan","fev","marc","abr","mai","jun","jul","ago","set","out","nov","dez"]
for chave in meses:
     meses[chave] = mesesNome[chave]
     print(meses)

print(meses.items())


for chave , valor in meses.items():
    print(chave, valor)


# UTILIZANDO MAX MIN LEN
print("Soma de todos:",sum(dictnumbers))
print("Quantidade de elementos:",len(dictnumbers))
print("Numero maior:",max(dictnumbers))
print("Numero menor:",min(dictnumbers))