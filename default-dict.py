"""
    COMO DEFAULT DICT AO PROCURAR UM ELEMENTO INEXISTENTE NAO OCORRER O ERROR KEYERROR
    PODE SER PASSADO COM PARAMETRO UMA FUNCAO LAMBDA QUE RECEBE UM VALOR PADRAO.


"""

from collections import defaultdict



dict_default = defaultdict(lambda:0)

dict_default["curso"]= "Python essencial"

print(dict_default["curso"])

print(dict_default["outro"]) #NAO RETORNA UM ERRO, E SIM UM VALOR PADRAO DEFINDO NA LAMBDA