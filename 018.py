# Recebe um âgulo qualquer e calcule o seno, cosseno e tangente

from math import radians,sin,cos,tan
a = float(input('Informe um ângulo qualquer: '))
r = radians(a)
s = sin(a)
c = cos(a)
t = tan(a)
print(
'''Para o ângulo {} temos:
Radianos:{}
Seno:{}
Cosseno:{}
Tangente:{}
'''.format(a,r,s,c,t))
