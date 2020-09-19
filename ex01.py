
carrinho = []
carteira = 20  #EM REIAS
valorgasto = 0.0



produtos = [
    {"prod":"Arroz", "valor":5.50, "cat":"alimento"},
    {"prod":"Macarrão", "valor":2.80, "cat":"alimento"},
    {"prod":"Feijão", "valor":4.35, "cat":"alimento"},
    {"prod":"Cream Crak", "valor":3.20, "cat":"alimento"},
    {"prod":"Bauduco", "valor":3, "cat":"alimento"},
    {"prod":"Açucar", "valor":4, "cat":"alimento"},
    {"prod": "Leite", "valor": 3.59, "cat": "alimento"},
    {"prod": "Batata doce kg", "valor": 1.98, "cat": "alimento"},
    {"prod": "Sal", "valor": 0.80, "cat": "alimento"}
]


for produto in produtos:
    print(produto)
    if produto.get("valor") <= carteira:
        carteira-= produto.get("valor")
        carrinho.append(produto)
        valorgasto= valorgasto + produto.get("valor")
        print(round(carteira, 2))  #METODO ROUND LIMITA A CASA DECIMAIS

    else:
        print(f"Voce nao possui dinheiro para o produto {produto.get('prod')} de valor :  {produto.get('valor')}")
        print(f" Seu dinheiro é : {round(carteira, 2)}")
        print(f" total de compras: {carrinho.__len__()} \n Valor total da compra: {valorgasto}")
        break

