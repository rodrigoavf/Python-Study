'''
Receba o ano de nascimento e informe:
- Se ele ainda vai se alistar ao serviço militar
- Se é hora de se alistar
- Se já passou do tempo de alistamento
'''
from datetime import date

while True:
    n = int(input('Qual seu ano de nascimento? '))
    y = date.today().year
    a = y-n
    if a == 18:
        print("Este ano você deve se alistar ao serviço militar!")
    elif a > 18:
        print('Já passou {} anos desde o seu alistamento.'.format(a-18))
    else:
        print('Ainda faltam {} anos para você se alistar'.format(18-a))