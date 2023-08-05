'''
Receba o peso e altura de uma pessoa e calcule o IMC
- Abaixo de 18.5 = Abaixo do peso
- Entre 18.5 e 25 = Peso ideal
- 25 até 30 = Sobrepeso
- 30 até 40 = Obesidade
- Acima de 40 = Obesidade mórbida
'''

p = float(input('Qual seu peso? '))
a = float(input('Qual sua altura? '))
imc = p / a**2
print('Seu imc é {:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
