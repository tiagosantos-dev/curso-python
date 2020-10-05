"""
Funcao seek -> le um arquivo apartir de um indice seek(0)
Funcao readLine() -  le apenas linha
funcao readLines() - retorna uma lista com todas as linhas

OBS: Quando abrimos um arquivo com a funcao open() é criada uma
conexao entre o arquivo no disco deo computador e o nosso programa.
esta conexao é chamada de streaming, ao finalizar os trabalhos com
o arquivo devemos fechar esse conexao. para isso utilizamos a funcao close()

"""

arquivo = open("texto.txt")
# print(len(arquivo.readlines())) Para saber a quantidade de linhas tem no arquivo
ret_linha = arquivo.readline()
lista_de_palavra = ret_linha.split()
print(lista_de_palavra)

print(arquivo.readlines())

# Funcao closed retorna false caso o arquivo esteja aberto
print("O arquivo esta fechado :?", arquivo.closed)

if not arquivo.closed:
    #Funcao close fecha a conexao entre o seu arquivo com o arquivo txt
    arquivo.close()
    print("e agr está fechado: ", arquivo.closed)


# Se tentarmos ler um arquivo ja fechado ocorrerá um erro
# ValueError: I/O operation on closed file.
# arquivo.read()


#OBS: COM A FUNCAO read() podemos limitar quantos caracters queremos que apareca read(50)
