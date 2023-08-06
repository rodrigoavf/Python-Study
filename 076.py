'''
Crie uma tupla com nomes de produtos e seus respectivos preços na sequência
Mostre os dados de forma tabular
'''

t = (
    "Lápis", 1.75,
    "Borracha", 2.0,
    "Caderno", 15.90,
    "Estojo", 25.00,
    "Transferidor", 4.20,
    "Compasso", 9.99,
    "Mochila", 120.32,
    "Canetas", 22.30,
    "Livro", 34.90
    )

i=0
print(f'{" LISTA DE PREÇOS ":=^50}')
while i < len(t)-1:
    print(f'{t[i]:.<40} R$ {t[i+1]:>6.2f}')
    i +=2