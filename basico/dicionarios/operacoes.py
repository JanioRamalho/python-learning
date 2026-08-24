### Adicionar, Remover e Modificar itens no Dicionário

lucro_1tri = {'Janeiro' : 100000 , "Fevereiro" : 120000 , "Março" : 90000}
lucro_2tri = {"Abril" : 88000 , "Maio" : 89000 , "Junho": 120000}  

# dicionario[chave] = valor
# dicionario.update(chave: valor)
# 1. Adicionando 1 item
lucro_1tri["Abril"] = 50000
print(lucro_1tri)

# 2. Adicionando vários itens ou um dicionário a outro
lucro_1tri.update(lucro_2tri)
print(lucro_1tri)


# 3. Modificar um item dentro do dicionário

# Da mesma forma que adicionamos 1 valor, caso essa chave já exista o item é apenas modificado.
#dicionario[chave] = valor

# 4. Modificar o lucro de fevereiro:

lucro_1tri["Fevereiro"] = 85000
print(lucro_1tri)


# 5. Remover itens:
# del dicionario[chave]
#        ou 
# valor = dicionario.pop(chave)

# Remover o mês de junho:
del lucro_1tri['Junho']
print(lucro_1tri)



### dicionario.clear() -> Vai limpar o dicionario, mas vai continuar existindo
### del dicionario -> Vai apagar o dicionario por completo, vai parar de existir