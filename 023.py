# Receba um número interiro de até 4 dígitos e mostre separadamente unidade, dezena, centena e milhar

n = int(input('Insire um número de 0 a 9999: '))
nstr = str(n)
print('Unidade:',nstr[-1])
print('Dezena:',nstr[-2])
print('Centena:',nstr[-3])
print('Milhar',nstr[-4])