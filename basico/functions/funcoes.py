# Retornar um número
def minha_soma(num1, num2, num3):
    return num1 + num2 + num3

print(minha_soma(3,4,6))


# Retornar um texto
def padronizar_texto(texto):
    texto = texto.casefold()
    texto = texto.replace("  ", " ")
    texto = texto.strip()
    return texto

print(padronizar_texto("  BOm dIA, peSSoaL"))


# Retornar um boolean
def bateu_meta(venda, meta):
    if venda > meta:
        return True
    else:
        return False

vendas_janio = 600
meta = 230

if bateu_meta(vendas_janio, meta):
    print("Janio Bateu a meta!")
else: 
    print("Janio não bateu a meta")


# Retornar uma lista, tupla ou dicionário
def filtrar_lista_texto(lista, pedaco_texto):
    lista_filtrada = []
    for item in lista:
        if pedaco_texto in item:
            lista_filtrada.append(item)
    return lista_filtrada # O return não pode ficar identado de qualquer forma

lista_emails = ['janio@gmail.com' , 'arthur@hotmail.com' ,'giovani@gmail.com' , 'igor@gmail.com' , 'diego@hotmail.com' ,'italo@yahoo.com']
print(filtrar_lista_texto(lista_emails , "gmail"))