# Receba um número inteiro e mostre na tela sua tabuada de 1 a 10

n = int(input('Digite um número inteiro para ver sua tabuada completa: '))
for i in range(11):
    print('{} x {} = {}'.format(n, i, n*i))
