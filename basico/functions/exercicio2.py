'''
Exercício 2 — Parâmetro com valor padrão

Crie uma função chamada formatar_nomes que receba:

1. Uma lista de nomes de clientes.
2. Um parâmetro chamado formato, cujo valor padrão deve ser "titulo".

A função deve remover os espaços no início e no fim de cada nome.

Quando formato for:
- "titulo": deixe a primeira letra de cada palavra maiúscula.
- "maiusculo": transforme todo o nome em letras maiúsculas.
- "minusculo": transforme todo o nome em letras minúsculas.

Ao final, a função deve retornar a lista com os nomes formatados.

Desafio: se o formato informado não for uma das três opções acima,
retorne a mensagem "Formato inválido".
'''

nomes_clientes = [
    "  maria da silva ",
    "JOÃO PEREIRA  ",
    "  ana BEATRIZ",
    "carlos eduardo "
]


def formatar_nomes(lista_nomes, formato="titulo"):
    # Escreva sua solução aqui.
    for i , nome in enumerate(lista_nomes):
        nome = nome.strip()
        if formato == "titulo":
            nome = nome.title()
        elif formato == "maiusculo":
            nome = nome.upper()
        elif formato == "minusculo":
            nome = nome.casefold()
        lista_nomes[i] = nome
    return lista_nomes

print(formatar_nomes(nomes_clientes))


# Teste a função usando o valor padrão.
#print(formatar_nomes(nomes_clientes.copy()))

# Depois, faça outros testes usando "maiusculo", "minusculo"
# e também um formato inválido.
