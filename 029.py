# Receba a velocidade de um carro, caso acima de 80kmh aplique uma multa de R$7 a cada kmh a mais de 80kmh

v = int(input('Qual a velocidade do carro?\n'))
if v > 80:
    print('O carro foi multado em R${}'.format((v-80)*7))
else:
    print('O carro está dentro do limite de velocidade de 80kmh')