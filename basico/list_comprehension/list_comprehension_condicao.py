# 1. Listas separadas para produtos e valores
produtos = ["Mouse Gamer", "Teclado Mecânico", "Mousepad Simples", "Headset 7.1", "Pendrive 32GB"]
precos = [1500, 3500, 300, 280, 450]
meta = 1000

#Usando o for normal:
lista_produtos = []
for i , produto in enumerate(produtos):
    if precos[i] > meta:
        lista_produtos.append(produto)
print("\nUsando for normal:")
print(lista_produtos)
print()

#Usando list comprehension:
print("Usando list comprehension:")
lista_produtos_2 = [produto for i, produto in enumerate(produtos) if precos[i] > meta]
print(lista_produtos_2)



