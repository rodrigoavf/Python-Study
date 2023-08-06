'''
Receba 4 valores do usuário e salve-os em uma tupla
Mostre:
- Quantas vezes apareceu o número 9
- Em que posição foi digitado o primeiro valor 3
- Quais foram os números pares
'''

t = tuple(int(input(f'Informe o {i+1}º valor ')) for i in range(4))

print(f'Os números digitados foram: {t}')

if 9 in t == 0:
    print('O número 9 não foi digitado nenhuma vez')
else:
    print(f'O 9 aparece {t.count(9)}')

if 3 in t == 0:
    print('O número 3 não foi digitado nenhuma vez')
else:
    print(f'O primeiro 3 aparece na posição {t.index(3)}')

l = []
for i in t:
    if i % 2 == 0: l.append(i)

if len(l) == 0:
    print('Nenhuma número par foi digitado')
else:
    print(f'Os números pares foram {l}')
