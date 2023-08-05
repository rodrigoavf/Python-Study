'''
Receba dois valores e mostre um menu na tela
print('[1] somar')
print('[2] multiplicar')
print('[3] maior')
print('[4] novos números')
print('[5] said o programa')
'''
c = 0
print('-='*40)
print('CALUCLADORA DE 2 NÚMEROS')
print('-='*40)
n1 = float(input('Informe o 1º número: '))
n2 = float(input('Informe o 2º número: '))

while c != 5:
    print('-='*40)
    print('Qual cálculo você quer realizar?')
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair o programa')
    c = int(input('Digite a opção desejada: '))
    print('\033[31m')
    match c:
        case 1:
            print('Resultado:')
            print(f'{n1} + {n2} = {n1+n2}')
        case 2:
            print('Resultado:')
            print(f'{n1} * {n2} = {n1*n2}')
        case 3:
            print('Resultado:')
            print(f'{max(n1,n2)}')
        case 4:
            n1 = float(input('Informe o 1º número: '))
            n2 = float(input('Informe o 2º número: '))
        case 5:
            print('Tchau tchau!')
        case _:
            print('Esta não é uma opção válida')
    print('\033[37m')