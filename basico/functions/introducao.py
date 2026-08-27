    # As funções servem para agrupar um conjunto de instruções para realizar uma tarefa especifica

# def nome_funcao():
#   faça alguma coisa
#   faça outra coisa
#   return valor_final

# Vamos criar uma função que cadastre produtos. Essa função deve garantir que o produto esteja com as letras em minusculo

def cadastrar_produto():
    produto = input("Digite o produto que deseja cadastrar: ")
    produto = produto.casefold() #Converte a string em letras minusculas
    print(f'{produto} foi cadastrado!')

for i in range(3):
    cadastrar_produto()



# Retornar valor com Function
# Usamos o return para devolver um resultado de dentro de função para que chamou essa função, ou seja, ela para ser usada fora 
# Da função precisa de um return   

# Função somar valores

def somar(a,b):
    resultado = a + b
    return resultado

valor = somar(3, 5)
print(valor)