nome = "Tiago Santos"

#Reversendo uma string

print(nome[::-1])

#Pegando apenas uma parte da palavra

print("Pegando do 0 a 5: ",nome[0:5])

#Trocando um caractere por outro

print("Metodo Replace: ",nome.replace('T','A'))

#superando cada palavra e colocando dentro do list
print("Metodo Split: ",nome.split())

#Adicionando uma nova palavra na parte de tras da string
print(nome.__add__(" Batista"))

#Deixando letras minusculas
print(nome.lower())

#Deixando letras Maisculas
print(nome.upper())

#Primeira letra da frase letra maiscula
print(nome.title())


