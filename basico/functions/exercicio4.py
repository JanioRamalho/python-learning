'''
Queremos criar uma function que consiga identificar os vendeores que bateram uma meta, mas além disso, consiga
já me dar como resposta o cálculo do % da lista de vendedores que bateu a meta( para eu não precisa calcular
manualmente depois)

Essa function deve receber 2 informações como parâmetro: a meta e um dicionário com os vendedores e suas vendas.
E me dar 2 respostas: uma lista com o nome dos vendedores que bateram a meta e o % de vendedores que bateu a 
meta
'''

meta = 10000
vendas = {
    'João' : 15000,
    'Julia' : 27000,
    'Marcus' : 9900,
    'Maria' : 3750,
    'Ana' : 10300,
    'Alon' : 7870,
}

#Crie a função
def calculo_meta(meta, vendas):
    bateram_meta = []
    for vendedor in vendas:
        if vendas[vendedor] > meta:
            bateram_meta.append(vendedor)
    percentual_meta = (len(bateram_meta) / len(vendas)) * 100
    return percentual_meta , bateram_meta 

percentual_meta , bateram_meta = calculo_meta(meta , vendas)
print(percentual_meta)
print(bateram_meta)
        


