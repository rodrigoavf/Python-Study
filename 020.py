# Receba o nome de 4 alunos e sortei a oordem em que eles apresentaram um trabalho

import random
n1 = input('Insira o nome 1: ')
n2 = input('Insira o nome 2: ')
n3 = input('Insira o nome 3: ')
n4 = input('Insira o nome 4: ')
nomes = [n1,n2,n3,n4]
random.shuffle(nomes)
print(nomes)
