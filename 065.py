'''
Receba vários números
Ao final mostre:
- Média entre todos os números
- Maior
- Menor
- Perguntar ao usuário se quer continuar ou não
'''
continuar = 'S'
l = []
print(f'{"Média, maior e menor":-^50}')
while continuar == 'S':
    l.append(float(input('Informe um número: ')))
    continuar = input('Deseja inserir outro número? [S/N]').upper()

print(f'{"Estatísticas":-^50}')
print(f'A média entra os números é {sum(l)/len(l)}')
print(f'O maior número é {max(l)}')
print(f'O menor número é {min(l)}')