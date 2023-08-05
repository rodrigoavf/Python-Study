# Receba o preço de um produto e calcule o valor com um desconto de 5%

p = float(input('Insira o preço do produto: '))
pdesc = p*.95
print('O preço com 5% de desconto para um produto cujo preço cheio é {} é {}'.format(p, pdesc))
