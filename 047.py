'''
Mostre todos os número pares entre 0 e 50
'''

print('Resolução usando IF (MENOS EFICIENTE)')
for i in range(0,51): # 51 por que o range o final não é inclusivo
    if i % 2 == 0:
        print(i, end = ' ') # end = ' ' faz que com tudo fique na mesma linha

print('Resolução usando um FOR que pula de 2 em 2 (MAIS EFICIENTE)')
for i in range(0,51,2):
    print(i, end = ' ') # end = ' ' faz que com tudo fique na mesma linha