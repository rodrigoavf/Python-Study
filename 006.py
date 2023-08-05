# Peça um número e retorne o seu dobro, triplo e raiz quadrada com 2 casas decimais

n = float(input('Insira um número: '))
print('Aqui estão o dobro, triplo e raiz quadrada de {}: \nDobro:{}\nTriplo:{}\nRaiz Quadrada:{:.2f}'.format(n,n*2,n*3,n**(1/2)))
