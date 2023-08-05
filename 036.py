'''
Pergunte o valor de uma casa e o salário do comprador
e em quantos anos ele pretende pagar.
Calcule o valor da prestação mensal sabendo que ela não
pode exceder 30% do salário ou o empréstimo será negado
'''

casa = float(input('Qual o valor do imóvel? '))
salário = float(input('Qual o salário do comprador? '))
anos = int(input('Qual a quantida de parcelas? '))
prestação = round(casa/(anos*12),2)
if prestação > salário*0.3:
    print('Empréstimo negado! A prestação excede 30% do salário')
else:
    print('Empréstimo pode ser concedido com uma prestação mensal de R${}'.format(prestação))
