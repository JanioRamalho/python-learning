'''
  - Dicionário com valores padrões:
dicionario = dict.fromkeys(lista_chaves , valor_padrao)

  - Dicionário a partir de listas de tuplas:
dicionario = dict(lista_tuplas)

  -Dicionario a paritr de 2 listas:
Passo 1: Transformar listas em lista de tuplas com o metodo zip
Passo 2: Transformar em dicionario

 lista_tuplas = zip(lista1 , lista2)
 dicionario = dict(lista_tuplas)
'''

produtos = [ "iphone",
    "samsung galaxy",
    "tv samsung",
    "ps5",
    "tablet",
    "ipad",
    "tv philco",
    "notebook hp",
    "notebook dell",
    "notebook asus"]

precos = [  15000,
    12000,
    10000,
    14300,
    1720,
    1000,
    2500,
    1000,
    17000,
    2450]


# Criar uma lista de tuplas
lista_tuplas = zip(produtos , precos)

# Transformar a lista de tupla em dicionario
dicionario_lista = dict(lista_tuplas)
print(dicionario_lista)