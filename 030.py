# Receba um número inteiro qualquer e diga se ele é IMPAR ou PAR

n = int(input('Digite um número inteiro qualquer:\n'))
if n%2 == 0:
    print('O número {} é par'.format(n))
else:
    print('O número {} é impar'.format(n))