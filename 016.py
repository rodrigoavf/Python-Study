# Receba um número real qualquer e retorne somente a parte inteira do número
from math import trunc
n = float(input('Informe um número real qualquer: '))
print('A parte inteira de {} é {}'.format(n,int(n)))
print('A parte inteira de {} é {}'.format(n,trunc(n)))