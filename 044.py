'''
Calcule o desconto e valor a ser pago por um produto dependendo 
da forma de pagamento
- Á vista em dinheiro ou cheque = 10%
- À vista no cartão = 5%
- Até 2x = 0%
- 3x ou mais = 20% de juros
'''

p = float(input('Qual o valor do produto? '))
d = int(input('''
Informe a forma de pagamento, selecionando uma das opções:
1 = Á vista no dinheiro ou cheque
2 = À vista no cartão
3 = 2x no cartão
4 = 3x ou mais no cartão
'''))

if d == 1:
    print('Desconto de 10%, total a pagar = R${:.2f}'.format(p*0.9))
elif d == 2:
    print('Desconto de 5%, total a pagar = R${:.2f}'.format(p*0.95))
elif d == 3:
    print('Total a pagar = R${:.2f}'.format(p))
elif d == 4:
    print('Juros de 20%, total a pagar = R${:.2f}'.format(p*1.2))
