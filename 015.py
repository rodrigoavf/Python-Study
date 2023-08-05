# Calcule o valor total do aluguel de um carro dado que a diária custa R$60 e o km rodado R$0.15

d = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos km rodou? '))
print('O valor total do aluguel para {} dias e {}km rodados é de R${}'.format(d,km,60*d+0.15*km))