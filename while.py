import math

print("Informe o valor de A  --")
a = float(input())

while a == 0:
    print("Informe o valor de A")
    a = float(input())
    if a == 0:
        print("não é permitido o valor zero")
        a = float(input())


    print("Informe o valor de B")
    b = float(input())

    print("Informe o valor de C")
    c = float(input())

sim_or_nao = input("Ja acabou jessica")

while sim_or_nao != "nao":
    sim_or_nao = input("Ja acabou jessica")


while True:
    result = input("Digite Sair para sair:")
    result= result.lower()
    if result == "sair":
        break
print("Bye")


