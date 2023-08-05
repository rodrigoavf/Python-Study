'''
Receba 6 número do usuário e mostre a some daqueles que são pares
'''

n = []
for i in range(1,7):
    n.append(int(input(f'Insira o {i}º número: ')))

for i in n:
    if i % 2 == 1: #Testando cada número da lista n se é impar
        n.pop(n.index(i)) #Remove da lista o número que é impar

print(f'Dentro os número digitados os seguintes eram par:\n {n}')

print(f'A soma destes números é {sum(n)}')
