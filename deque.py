"""
PODEMOS DIZER QUE DEQUE E UMA LISTA DE ALTA PERFOMANCE

"""
from collections import  deque
#CRIANDO DEQUES


lista = ["arroz", "feijao ", "açucar", "leite"]

#REMOVENDO E RETORNA O ULTIMO
retorno = lista.pop()
print(retorno)


dequee = deque(["arroz", "feijao ", "açucar", "leite"])

print(dequee)

#APAGA E RETORNA O PRIMEIRO
retorna_primeiro= dequee.popleft()
print(retorna_primeiro)

#INSERE NO PRIMEIRO ELEMENTO
dequee.appendleft("No lugar do arroz coma macarao")
print(dequee)