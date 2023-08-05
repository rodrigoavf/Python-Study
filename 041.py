'''
Leia o ano de nascimento de um atleta e defina sua categoria
Até 9 anos = Mirim
Até 14 anos = Infantil
Até 19 anos = Junior
Até 20 anos = Sênior
Acima de 20 = Master
'''
import datetime
a = int(input('Informe o ano de nascimento do atleta: '))
idade = datetime.date.today().year - a
print('O atleta tem {} anos e sua categoria é:'.format(idade))
if idade <=9:
    print('Mirim')
elif idade <=14:
    print('Infantil')
elif idade <=19:
    print('Junior')
elif idade <=20:
    print('Sênior')
else:
    print('Master')
