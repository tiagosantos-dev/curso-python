"""
Comandos basicos do PDB
l (Lista onde estamos no codigo)
n {proxima linha}
p (imprime variaveis)
c (continua a execucao)

OBS:comando para ver a varivel utlize "p  nome_da_variavel"

a partir da versao 3.7 do python a biblioteca pdb foi integrada a linguagem
e podemos apenas chamar o metodo breakpoint()
"""
import pdb

nome = "Tiago"
sobrenome = "Santos"
#pdb.set_trace()
breakpoint()
nome_completo = nome+" "+sobrenome
curso = "Python Essencial"


def dividir(a, b):
    try:
        return a/b
    except (ValueError, ZeroDivisionError) as err:
        print(f"Error ao dividir motivo do erro: {err}")


dividir(0, 0)
