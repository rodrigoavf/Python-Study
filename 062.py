'''
Receba o primeiro termo e a razão de uma PA
Exiba os 10 primeiros termos dessa PA usando WHILE
E pergunte ao usuário se ele quer ver o próximo número da PA

Encerre o programa quando o usuário disser não
'''

adicional = 10
inicial = 0

print(f'{"CALCULADORA DE PA":-^50}')

n = int(input('Insira o primeiro número de uma PA: '))
r = int(input('Informe a razão dessa PA: '))

print('Os 10 primeiro números desta PA são: ')
while inicial < 10:
    print(n+r*inicial)
    inicial += 1

while adicional > 0:
    adicional = int(input('Deseja ver mais quantos números desta PA? '))
    if adicional == 0:
        print(f'{"PROGRAMA ENCERRADO":-^50}')
        break
    for i in range(inicial,inicial+adicional):
        print(n+r*i)
    inicial += adicional