'''
Receba um número inteiro qualquer n
Mostre os n primeiros números de um sequeência de fibonacci
'''
print(f'{"SEQUÊNCIA DE FIBONACCI":-^50}')
n = int(input('Quantos números da sequência de Fibonacci você quer ver? '))

n1 = 0
n2 = 0
n3 = 0

print(f'Os {n} primeiros números de Fibanacci são:')
for i in range(n):
    print(f'{n3}')
    n3 = 1 if n3 == 0 else n1 + n2
    n1 = n2
    n2 = n3