# lista = [Expressão for item in iterable]

preco_produto = [100, 150, 300, 5500]
produtos = ['Vinho', 'Cafeiteira', 'Cerveja', 'Carro']
'''
Imposto sobre os produtos é de 30%. Como eu faria para criar uma lista com os valores de imposto de cada produto?
'''
#Com a maneira tradicional, usando o for:
imposto = []
for preco in preco_produto:
    imposto.append(preco * 0.3)
print(imposto)


#Usando list comprehension:
lista_imposto = [item * 0.3 for item in preco_produto]
print(lista_imposto)


def calcular_imposto(preco, imposto):
    return preco * imposto

lista_imposto_funcao = [calcular_imposto(preco, 0.3) for preco in preco_produto]
print(lista_imposto_funcao)