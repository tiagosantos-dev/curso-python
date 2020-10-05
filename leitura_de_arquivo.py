"""
Funcao open() =-> Por padrao a funcao open abre o arquivo para leitura.
este arquivo deve existir  ou entao teremos o erro fileNotFoundError

retorno <_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>
mode= "r" significa - read() / modo leitura

"""

texto = open("texto.txt", encoding="UTF-8")
print(texto)
#Para ler um arquivo precisa chama a funcao read()
print(texto.read())
var = texto.read()
print("Var: ", var)


print(type(texto.read()))

#OBS: O python utiliza um recurso para trabalhar
# com arquivos chamado cursor, ou seja ele ler tudo
