"""
Try / Excepet - utiizamos para tratar erros que podem ocorrer no nosso codigo
try:
    codigo perigoso
except:
    se acontecer o erro
"""


try:
   geek()
except NameError:
    print("Deu um problema")

try:
   len(12)
except TypeError as err:
    print(f"Funcao len só permite parametros contaveis : tipo do eror - {err}")


def pegando_valores(dictt, chave):
    try:
       return dictt[chave]
    except KeyError as key_error:
        print(f"Erro na chave: {key_error}")
    except TypeError as typeError:
        print(f"Erro ao passar o iteravel: {typeError}")
    except NameError as nameError:
        print(f"Erro ao passar o iteravel: {nameError}")
    except :
        print(f"Error Desconhecido")


dictt = {"Tiago": "Santos"}

print(pegando_valores(dictt, "Vai da error"))
print(pegando_valores(dictt, "Tiago"))
print(pegando_valores(123, "Tiago"))
print(pegando_valores(fsdfsdf, "Tiago"))
