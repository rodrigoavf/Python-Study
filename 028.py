# Gere um número aleatório entre 0 e 5 e tente adivinhar o número sorteado.
import random

print("Acabei de pensar em número de 0 a 5")
n = random.randint(1,5)
a = int(input('Qual número eu pensei?\n'))
if a == n:
    print('Wow, você acertou, eu havia pensado no número {}'.format(n))
else:
    print('Você errou, eu havia pensado no número {}'.format(n))