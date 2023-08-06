'''
Gere 5 números aleatórios e coloque-os em uma tupla
Mostre: 
- A lista de números gerados
- Maior
- Menor
'''

from random import randint

numeros = tuple(randint(0,1000) for i in range(5))

print(numeros)
print(f'O maior é: {max(numeros)}')
print(f'O menor é: {min(numeros)}')