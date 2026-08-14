produtos = ['apple tv' , 'mac' , 'iphone x' , 'iphone 11' , 'Ipad' , 'apple watch' , 'mac book']
print(produtos)

# O que foi colocado antes do join vai ser o que separa os elementos da lista
# \n é equivalente ao enter
print('\n'.join(produtos))

print(" - ".join(produtos))

# Split
produtos = 'apple tv, mac, iphone x, iphone 11, Ipad, apple watch, mac book'
lista_splitada = produtos.split(", ")
print(lista_splitada)