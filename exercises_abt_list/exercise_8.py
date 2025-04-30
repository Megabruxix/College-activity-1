precos = ["11", "22", "34","47", "50"]
for valor in precos:
    preco = int(valor)
    desconto = preco * 0.10
    preco_final = preco - desconto
    print(preco_final)