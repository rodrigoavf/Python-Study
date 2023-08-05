'''
Receba nome e preço de vários produtos
A cada novo produto pergunte se deseja fechar a conta ou adicionar mais produtos
Ao final mostre:
- Qual o total da compra
- Quantos produtos custam mais de 1000
- Qual o nome do produto mais barato
'''
import pandas as pd

produtos = pd.DataFrame(columns=['Produto','Preço'])

print(f'{"Lista de compras":=^50}')
while True:
    c = ''
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço do produto: R$ '))
    produtos.loc[len(produtos)] = [produto,preço]
    while c not in ['S','N']:
        c = str(input('Deseja cadastrar mais algum produto? [S/N] ')).upper()
    if c == 'N': break
print("="*50)
print('')
print(f'Total da compra: R$ {produtos["Preço"].sum()}')
print(f'Produtos que custam mais de R$ 1.000,00: {len(produtos[produtos["Preço"]>1000])}')
print(f'O produto mais barato é {produtos[produtos["Preço"]==produtos["Preço"].min()]["Produto"].iloc[0]}')
print(f'O produto mais caro é {produtos[produtos["Preço"]==produtos["Preço"].max()]["Produto"].iloc[0]}')
