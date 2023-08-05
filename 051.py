'''
Receba o primeiro termo e a razão de uma PA
Exiba os 10 primeiros termos dessa PA
'''

n = int(input('Insira o primeiro número de uma PA: '))
r = int(input('Informe a razão dessa PA: '))

print('Os 10 primeiro números desta PA são: ')
for i in range(0,10):
    print(n+(r*i))