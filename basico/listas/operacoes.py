'''
insert()
pop()
index()
count()
sort()
reverse()
extend()
'''


produtos_eletronicos = [
    "Computador",
    "Celular",
    "Televisão",
    "PlayStation",
    "Geladeira",
    "Nobreak"
]

# 1. INSERT
# Adciona um objeto á uma posição escolhida
# O objeto que ocupava a posição original, passa para a seguinte

produtos_eletronicos.insert(2, "Telão")
print(produtos_eletronicos)


# 2. POP 
# Remove o último objeto da lista
# Não podemos escolher o que vai sair. Sempre será o último objeto
# EX: produtos_eletronicos.pop("Geladeira") --> ERRO

produtos_eletronicos.pop()
print(produtos_eletronicos)


# 3. INDEX
# Retorna o índice do objeto desejado mais próximo
# Podemos usar um limite de ínicio e fim para selecionar o valor até certo intervalo
# [objeto : inicio : fim]

posicao_computador = produtos_eletronicos.index("Computador")
print(posicao_computador)

# Vamos criar uma lista com numeros para o próximo exemplo:

lista_num = [0,5,3,6,8,3,1,4,6,1,4,3,5,7,2]

'''
O que faremos é verificar o tamanho da nossa lista. Logo a seguir, vamos criar uma variável 
que receberá o primeiro índice do objeto desejado. No nosso caso o número "1". 
O número 1 aparece no índice 6 e 9, porém o index() pega somente o índice mais próximo

[0,5,3,6,8,3,1,4,6,8,4,3,5,7,2]
'''
print(len(lista_num))
posicao_num = lista_num.index(1, 2, 15)
print(posicao_num)



# 4. COUNT 
# Serve para contar elementos em uma lista
print(lista_num.count(1))


# 5. SORT
# O sort() é um método de listas usado para ordenar os elementos da própria lista.
# Por padrão, ele ordena de forma crescente

lista_num.sort()
print(lista_num)


# 6. REVERSE
# O reverse vai inverter a lista
# O primeiro índice da lista era o último 

animais = ["Cachorro" , "Papagaio" , "Gato" , "Elefante" , "Jacaré"]
print(f'Antes do Reverse: {animais}')
animais.reverse()
print(f'Depois do Reverse: {animais}')


# 7. EXTEND
# O extend geralmente é usado para unir duas listas de uma mesma natureza
# Não tem a mesma lógica do append
 
uf1 = ["RN" , "CE" , "PB" , "RJ"]
uf2 = ["SP" , "BA" , "ES" , "AM"]

uf1.extend(uf2)
print(uf1)