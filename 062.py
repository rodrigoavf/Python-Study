'''
Receba o primeiro termo e a razão de uma PA
Exiba os 10 primeiros termos dessa PA usando WHILE
E pergunte ao usuário se ele quer ver o próximo número da PA

Encerre o programa quando o usuário disser não
'''

n = int(input('Insira o primeiro número de uma PA: '))
r = int(input('Informe a razão dessa PA: '))

print('Os 10 primeiro números desta PA são: ')
i = 0
c = 'S'
while i < 10:
        print(n+(r*i))
        i += 1
while c != 'N':
    c = str(input('Deseja ver o próximo númeo da PA? [S/N]')).upper()
    match c:
        case 'S':
            i += 1
            print(f'O {i}º número desta PA é: {n+(r*i)}')
        case 'N':
            print('Tchau')
        case _:
            print('Opção não válida')
#oi