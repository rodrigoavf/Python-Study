'''
Receba o primeiro termo e a razão de uma PA
Exiba os 10 primeiros termos dessa PA usando WHILE
'''

n = int(input('Insira o primeiro número de uma PA: '))
r = int(input('Informe a razão dessa PA: '))

print('Os 10 primeiro números desta PA são: ')
i = 0
while i < 10:
    print(n+(r*i))
    i += 1