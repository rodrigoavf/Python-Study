'''
Mostre o fatorial de um número inserido pelo usuário
Por Exemplo:
5! = 5x4x3x2x1=120
'''

t = ''
f = 1
n = int(input('Insira um número inteiro maior que 0 para calcular seu fatorial: '))
print(f'O fatorial de {n} é:')
while n != 0:
    if t == '':
        t = n
    else:
        t = f'{t}x{n}'
    f *= n
    n -= 1
print(f'{t} = {f}')