
def quadrado(number):
    return number ** 2


result = quadrado(5)
print(result)


def cantar_parabens(aniversariante):
    print(f'Parabens pra vc, nessa data ... {aniversariante}')


cantar_parabens("Tiago")


def nome_completo(nome, sobrenome):
    print(f"Seu nome é : {nome}, sobrenome : {sobrenome}")


nome_completo("Tiago", "Santos")
nome_completo(nome="Joao", sobrenome="Batista")
nome_completo(sobrenome="Santos", nome="Tiago")

nome_fora = "Lucas"
sobrenome_fora = "Santos"
#PEGANDO VALOR DECLARADO EXTERNO
nome_completo(nome=nome_fora, sobrenome=sobrenome_fora)



