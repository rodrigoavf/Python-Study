# Pegue a largura e altura de uma parede calcule sua área e quantos litros de tinta são necessários para pintar a parede, sabendo que 1 litro pinta 2m²

a = float(input('Informe a altura da parede: '))
l = float(input('Informe a largura da parede: '))
mm = a*l
t = mm/2
print('Para uma parede com {} de altura e {} de largura temos:\nÁrea = {}\nQtd de tinta necessária = {} litros'.format(a, l, mm, t))
