'''   Função para cálculo de Carga Tributária
Imagine que você trabalha no setor contábil de uma grande empresa de Varejo.
Crie uma function que calcule qual o % de carga tributária que está sendo aplicado sobre um determinado produto, dado o preço 
de venda, o "lucro" e os custos (com exceção do imposto) dele.

'''

preco = 1500
custo = 400
lucro = 800

# O lucro não é o preço - custo, porque aidna tem o imposto
# Sua função deve calcular qual foi o % de imposto aplicado sobre o preço total

def carga_tributaria(preco, custo, lucro):
    lucro_parcial = preco - custo
    imposto = lucro_parcial - lucro
    carga = (imposto / preco) * 100
    return carga

print(carga_tributaria(preco, custo, lucro))