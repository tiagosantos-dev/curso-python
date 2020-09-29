"""
FILTER : SERVE PARA FILTRAR UM ITERAVEL, NO PRIMEIRO PARAMETRO A EMPRESSAO NO SEGUNDO O ITERAVEL
RETORNA UM FILTER OBJECT

"""
import statistics

# FORMA DE ITERACAO UTILIZANDO LIST COMPREENSHION
alunos = [{"aluno A": 10}, {"aluno B": 5.5}, {"aluno C": 8.9}, {"aluno D": 3}, {"aluno E": 6.7}, {"aluno F": 0}]
media = round(statistics.mean([ele for elemento in alunos for ele in elemento.values()]), 2)
print(media)
aprovados = [elemento for elemento in alunos for dic in elemento.values() if dic > media]
print(aprovados)


#UTILIZANDO O FILTER
def filtrado(ee):
    for valor in ee.values():
        if valor > media:
            return True


aprovados_filter = filter(filtrado, alunos)
print(list(aprovados_filter))
print(alunos[0].values())

#EXEMPLO 2
paises = ["", "Paraguai", "", "Argentina", "", "Uruguai", "", "", "Alemanha", "", "Portugal", "Brasil", "", "", ""]
print(paises)

#RETIRA OS VALORES NULOS
paises_filtrados = filter(None, paises)
print(list(paises_filtrados))


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

# 1 FORMA
inative_users = list(filter(lambda x: len(x["posts"]) == 0, users))
# 2 FORMA
inative_users_dois = list(filter(lambda x: not x["posts"], users))
print(inative_users)
print(inative_users_dois)


#UITLIZANDO MAP E FILTER

fist_name_pt = ["Ana", "tiago", "joao", "big", "eric", "cli", "jo", "pedro", "sayonara", "bob", "jecival"]


fist_name_en = list(map(lambda x: x.title()+"'s", filter(lambda x:  len(x) > 3, fist_name_pt)))
print(fist_name_pt)
print(fist_name_en)
