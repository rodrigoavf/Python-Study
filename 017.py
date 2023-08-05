# Calcule a hipotenusa de um triângulo retangulo dado os catetos

from math import hypot
co = float(input('Informe o tamanho do cateto oposto: '))
ca = float(input('Informe o valor do cateto adjacente: '))
h_manual = (ca**2 + co**2)**(1/2)
h_auto = hypot(ca,co)
print('A hipotenusa de um triângulo retângulo com catetos {} e {} é {}'.format(ca,co,h_manual))
print('A hipotenusa de um triângulo retângulo com catetos {} e {} é {}'.format(ca,co,h_auto))