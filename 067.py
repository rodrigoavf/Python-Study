'''
Mostre a tabuada de vários números, um de cada vez conforme solicitado pelo usuário
O programa é encerrado se o usuário digitar um valor negativo
'''

print(f'{"TABUADAS":=^50}')

while True:
    print('-'*50)
    n = int(input('Qual número quer ver a tabuada (<0 para encerrar): '))
    print('-'*50)
    if n < 0: break
    for i in range (0,11):
        print(f'{i} x {n} = {i*n}')
print('TCHAU!')