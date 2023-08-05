'''
Receba 3 comprimentos de reta e diga se formam um riângulo
E diga se é um triângulo:
Equilátero (Todos os lados são iguais)
Isósceles (Dois lados iguais)
Escaleno (Todos os lados diferentes)
'''

r1 = int(input('Tamanho da reta 1: '))
r2 = int(input('Tamanho da reta 2: '))
r3 = int(input('Tamanho da reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r2 and r3 < r1 + r3:
    if r1 == r2 == r3:
        print('Estas retas formam um triângulo equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Estas retas formam um triângulo isósceles')
    else:
        print('Estas retas formam um triângulo escaleno')
else:
    print('Estas restas não formam um triângulo.')