# Receba a distância de uam viagem, para viagens até 200km o preço por km é 0.5, para mais é o.45. qual o custo total da viagem?

d = int(input('Qual a distância da viagem?\n'))
c = 0.5
if d>100:
    c=0.45
print('O custo da viagem é {}'.format(d*c))
