# Receba o salário de um funcionário e calcule o valor de seu aumento
# Para salários maiores que 1250 calcule um aumento de 10%
# Para salário inferiores, calcule um aumento de 15%

s = float(input('Informe o salário do funcionário: '))
if s > 1250:
    print('Novo salário = R$ {:.2f}'.format(s*1.10))
else:
    print('Novo salárop = R$ {:.2f}'.format(s*1.15))
