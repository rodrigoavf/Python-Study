'''
Receba 2 números inteiros e compare-os
Mostre na tela uma mensagem:
- O primeiro valor é ....(maior ou menor)
- O segundo valor é ....(maior ou menor)
- Os dois valores são iguais
'''

while True:
    n1 = int(input('Insira o 1º número: '))
    n2 = int(input('Insira o 2º número: '))

    if n1 > n2:
        print('O primeiro valor é maior que o segundo.')
    elif n1 < n2:
        print('O segundo valor é maior que o primeiro.')
    else:
        print('Os dois valores são iguais')

    print('\n')