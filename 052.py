'''
Receba um número inteiro e diga se ele é primo ou não
'''

n = int(input('Digite um número int positivo: '))
primo = True
for i in range(2,n):
    if n % i == 0:
        primo = False
texto = 'não ' if primo == False else ''
print(f'{n} {texto}é um número primo ')