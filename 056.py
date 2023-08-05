'''
Receba o nome, idade e sexo de 4 pessoas
Indique:
- A média de iadade do grupo
- O nome do homem mais velho
- Quantas mulheres têm menos de 20 anos
'''
from statistics import mean

nome = []
idade = []
sexo = []

for i in range(0,4):
    print(f'Informe os dados da {i+1}ª pessoa:')
    nome.append(str(input('Nome: ')))
    idade.append(int(input('Idade: ')))
    sexo.append(str(input('Sexo [M/F]: ')))

homens = [(n, i) for n, i, s in zip(nome, idade, sexo) if s == 'M']
homens_nome, homens_idade = zip(*homens)
mulheres = [(n, i) for n, i, s in zip(nome, idade, sexo) if s == 'F']
mulheres_nome, mulheres_idade = zip(*mulheres)

print(f'A média de idade do grupo é: {mean(idade):.2f}')
if sexo.count('M') == 0:
    print('Não existem homens no grupo para idenficar qual é o homem mais velho.')
else:
    print(f'O homem mais velho do grupo é {homens_nome[homens_idade.index(max(homens_idade))]} com {max(homens_idade)} anos.')

if sexo.count('F') == 0:
    print('Não existem mulheres no grupo.')
else:
    print(f'A quantida de mulheres com menos de 20 anos é {sum(1 for i in mulheres_idade if i < 20)}')
