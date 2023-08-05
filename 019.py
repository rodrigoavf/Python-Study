# Receba 4 nomes do usuário e sorteie um deles
import random
n1 = input('Insira o nome 1: ')
n2 = input('Insira o nome 2: ')
n3 = input('Insira o nome 3: ')
n4 = input('Insira o nome 4: ')
nomes = [n1,n2,n3,n4]
print('O nome escolhido é: {}'.format(random.choice(nomes)))