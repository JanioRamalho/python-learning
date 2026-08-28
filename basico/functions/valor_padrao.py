'''
Tem alguns parâmetros que já possuem seus valores padrões, exemplo: .sort()
O sort vai tem como valor padrão "sort(reverse = False)", ou seja, ele por padrão vai atuar de forma crescente.
Para que ele atue de forma decrescente precisamos alterar esse valor padrão, para isso fazemos, "sort(reverse = True)"
'''

lista_num = [1,2,3,5,7,8,9,435,2,53,155,122]
lista_num.sort() # Crescente
print(lista_num)

lista_num.sort(reverse= True) # Decrescente
print(lista_num)


# Vamos criar uma função para padronizar os códigos de produtos. O default será padronizar os códigos para letras minúscula("m"),
# mas se o usuário quiser pode padronizar para maiúsculo, dado por (M)



def padronizar_codigo(lista_codigo , padrao = "m"):
    for i , item in enumerate(lista_codigo):
        item = item.replace("  " , " ")
        item = item.strip()
        if padrao == "m":
            item = item.casefold()
        elif padrao == "M":
            item = item.upper()
        lista_codigo[i] = item #Strings são imutaveis, para fazer alterações precisamos associar o indice do item com o item tratado        
    return lista_codigo

cod_produtos = [' ABC12' , 'abc34' , "Abc37"]
print(padronizar_codigo(cod_produtos, "m"))