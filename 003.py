# Peça dois números ao usuário e some estes dois números

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
print('Sem usar format:')
print('A soma entre',n1,'e',n2,'é',s)
print("Usando format:")
print('A soma entre {} e {} é {}'.format(n1, n2, s))