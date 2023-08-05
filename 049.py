# Receba um número inteiro e mostre na tela sua tabuada de 1 a 10 usando for

n = int(input('Digite um número inteiro para ver sua tabuada completa: '))
for i in range(11):
    print(f'{n} x {i} = {n*i}')
