"""
Modulo Collections > Counter(Contador)

Collections -> High-Perfomance Container Datetypes (Tipos de dados container em alta perfomace)

Recebe um iteravel como parametro e crua um objeto do tipo collection counter é parecido com um dicionario contendo
como chave o elemento  da lista passada como paraametro e como valor a quantidade de ocrrencia desse elemento
"""

from collections import Counter

# EXEMPLO 1
lista = [1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,5,5,5,6,7,7,8,8,8,8,66,6,5,544,5,54,5435435]

#Retorna um valor tipo dicionario, sendo a chave e o elemento , e o valor e a quantidade de vezes que se repetiu
counter = Counter(lista)
print(counter)

# EXEMPLO 2

nome = "Tiago Santos Batista AAAA"
nome_counter = Counter(nome)
print(nome_counter)


#EXEMPLO 3

texto ="""
    Mais uma noite como todas as anteriores. Pego minha caneca de café cheia, acendo meu ultimo 
    cigarro e corro pra velha janela do quarto. Observo a noite fria e chuvosa, até parece confortável 
    por um momento, se não fossem as dezenas de preocupações que me desmotivam a cada dia.
    Penso em você, mesmo sabendo o quão longe está de mim, sinto aquele amor que continua a me desgraçar 
    intensamente a cada dia, e penso quando enfim poderei te ter comigo. Sei lá, o café chega ao fim e trago 
    a ultima ponta, nada muda. É como se eu fosse passar por isso mais uns longos anos a frente.
    Cada vez mais tenho a sensação de incertezas e inseguranças e tento me manter firme apesar disso. Algumas
    coisas parecem dar certo e maioria não, tipo você.
    Então após 10 minutos refletindo, largo tudo, fecho a janela e volto pro meu mundo dentro do quarto.
    Não sei até quando, não sei o porquê, só sei que tá tudo tão errado e quero me livrar disso o quanto antes.
    E tu não tem nem ideia do quanto, amor meu.
"""
texto = texto.split()
# print(texto)

texto_counter = Counter(texto)
print(texto_counter)  # CONTA CADA PALAVRA  DO TEXTO

#PEGANDO AS X  PALAVRAS MAIS USADA
x_palavras = texto_counter.most_common(5)
print(x_palavras)

