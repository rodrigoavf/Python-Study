'''
Receba o sexo de uma pessoa, aceitando somente M e F
Caso não seja uma dessas opções, peça que digite novamente, até ser uma opção válida
'''
s = ''
while s not in ['M','F']:
    s = input('Qual seu sexo? [M/F] ')
    if s not in ['M','F']:
        print('Esta não é uma opção válida, escolha M ou F')

print(f'Legal, seu sexo é {s}')
