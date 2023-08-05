'''
Receba o ano de nascimento de 7 pessoas
Informe quantas delas já atingiram a maioridade, e quantas ainda não
'''

from datetime import date

ano = date.today().year
maior = 0
menor = 0

for i in range(0,7):
    if ano - int(input(f'Qual o ano de nascimento da {i+1}ª pessoa? ')) >=18:
        maior += 1
    else:
        menor += 1
print(f'Existem {maior} maiores de idade, e {menor} menores de idade')
