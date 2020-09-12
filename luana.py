print("Tabuada do numero:") #APARECERA NA TELA
tab = input() #PEGA O VALOR DIGITADO
tab = int(tab) #TRANSFORMA O VALOR DIGITADO EM NUMERO INTEIRO

for n in range(1000):
    print(tab,"+",n+1 , "=", tab+(n+1))
