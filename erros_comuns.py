"""
Erros mais comuns em Python

1 - NameError -  Quando existe um erro no nome da funcao, ou variavel  (nao foi definida)
    ex: printf() - Funcao nao existe

2- SyntaxError - Algo que o python nao reconhece como parte da linguagem
    ex: def = 1

3 - TypeError -  Quando uma funcao/aplicacao/operacao é aplicada a um tipo errado
    ex: len(24)

4 -  IndexError - Ocorre quando um indice de algum elemento é invalido (inexistente)
    ex: lista =["Aula"] print(lista[3])

5 - ValueError - Ocrre quando uma funcao/operacao buit-in
 recebe um argumento com tipo correto mas valor inapropiado
    ex: print(int("sadas"))

6 - KeyError - Ocorre quando tentamos acessar um dicionario com uma chave que nao existe
    ex: acessar um dicionario que nao existe chave

7 - AtributeError - Ocorre quando uma variaveel nao tem um atributo/funcao
    ex: acessar uma funcao inexistente em um elemento


8 - IndentationError - Espacamento para indentifcar cada funcao e etc (4 espaços)
    ex: def fazeralgo()
        print("fazendo algo')
"""
