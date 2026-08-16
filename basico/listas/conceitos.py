'''
Irei apresentar um pouco do que podemos fazer com as listas de forma mais direta aqui.
Para explicações mais detalhadas: abrir arquivo ".ipynb", lá poderei explicar melhor pois existem formas de
criar células de Markdown e código, logo a explicação fica bem mais organizada.
Aqui eu colocarei códigos e comentários, porém não chega a ser tão didático como o Jupyter.
'''

# Imagine que queremos fazer uma lista de produtos eletrônicos de uma loja.


# 1. CRIAÇÃO DE UMA LISTA
# Aqui você já apresenta como criar uma lista em Python utilizando colchetes [].

produtos_eletronicos = [
    "Computador",
    "Celular",
    "Televisão",
    "PlayStation",
    "Geladeira",
    "Nobreak"
]


# 2. TAMANHO DA LISTA
# len() retorna a quantidade de elementos presentes na lista.

print(len(produtos_eletronicos))


# 3. ACESSO A ELEMENTOS PELO ÍNDICE
# Os índices de uma lista começam em 0.
#
# Computador  -> índice 0
# Celular     -> índice 1
# Televisão   -> índice 2
# PlayStation -> índice 3
# Geladeira   -> índice 4
# Nobreak     -> índice 5

print(produtos_eletronicos[0])
print(produtos_eletronicos[3])
print(produtos_eletronicos[4])
print(produtos_eletronicos[1])


# 4. SLICING (FATIAMENTO)
# Permite acessar uma parte da lista.

print(produtos_eletronicos[0:3])
# Pega os elementos do índice 0 até o índice 2.
# O índice 3 não é incluído.


print(produtos_eletronicos[:])
# Retorna todos os elementos da lista.


# 5. ÍNDICES NEGATIVOS
# Índices negativos permitem acessar elementos começando pelo final da lista.

print(produtos_eletronicos[-1])
# -1 representa o último elemento da lista.


# 6. SLICING COM STEP
# O terceiro valor determina de quantos em quantos elementos o Python irá percorrer.

print(produtos_eletronicos[0:5:2])
# Começa no índice 0, vai até antes do índice 5 e avança de 2 em 2.


# 7. ÍNDICES NEGATIVOS
# Começa com -1 e é atribuído ao último objeto da lista e segue a contagem da direita para esquerda
# COMPUTADOR, CELULAR, TELEVISÃO, PLAYSTATION, GELADEIRA, NOBREAK
#    -6         -5        -4           -3         -2        -1



# 8. ALTERANDO ELEMENTOS
# Colocamos nossa lista e o índice do objeto que vamos trocar
# E atribuímos ao novo objeto

(produtos_eletronicos[1]) = "SmartPhone"

print(produtos_eletronicos)
# Listas são mutáveis. Agora nosso Índice 1 recebe "SmartPhone"


# 9. ADICIONANDO UM ELEMENTO

produtos_eletronicos.append("Notebook")

print(produtos_eletronicos)
# Notebook foi adicionado ao final da lista
# o metódo append() recebe um parâmetro e o inclui ao final da lista


# 10. REMOVENDO UM ELEMENTO

produtos_eletronicos.remove("Geladeira")
print(produtos_eletronicos)


# 11. PASSANDO POR CADA OBEJTO
# Usamos o for each para percorrer toda a lista

for produto in produtos_eletronicos:
    print(produto)

# O for each é muito interessante, pois ele cria uma variavel que recebe cada produto da lista
# produto = todos objetos da lista


