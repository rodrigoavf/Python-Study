'''
Receba a idade e sexo de várias pessoas
A cada pessoa cadastrada o programa deve perguntar se o usuário quer continuar cadastrando +
Ao final mostre:
- Quantas pessoas tem mais de 18 anos
- Quantos homens foram cadastrados
- Quantas mulheres tem menos de 20 anos
'''

import pandas as pd

df = pd.DataFrame(columns=['Sexo','Idade'])
s = ''
continuar = ''

print(f'{" CADASTRO DE PESSOAS ":=^50}')
while True:
    print(f'Insira os dados da {len(df)+1}ª pessoa')
    while s not in ['F','M']:
        s = input('Sexo: [M/F] ').upper()
    i = int(input('Idade: '))
    df.loc[len(df)] = [s,i]
    
    while continuar not in ['S','N']:
        continuar = str(input('Deseja cadastrar mais pessoas? [S/N]')).upper()
    if continuar == 'N': break
    s = ''
    continuar = ''
    print("."*50)

print(f'{" Estatísticas ":=^50}')
print(df)
print('.'*50)
print(f'Pessoas com mais de 18 anos: {len(df[df["Idade"]>18])}')
print(f'Homens: {len(df[df["Sexo"]=="M"])}')
print(f'Mulheres com menos de 20 anos: {len(df[(df["Sexo"]=="F") & (df["Idade"]<20)])}')
print('.'*50)
