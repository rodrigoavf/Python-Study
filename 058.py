'''
Gere um número aleatório de 0 a 10
Peça ao usuário digitar um número para tentar adivinhar o que o computador escolheu

Peça ao jogador quantas números forem necessários, até que ele acerte e diga quantas tentativas foram necessários para acertar
'''

from random import randint

r = randint(0,10)
n = -1
c = 0
print('Eu acabei de pensar em um número de 0 a 10')
print('Qual número você acha que eu pensei? ')

while n != r:
    n = int(input('Digite um número de 0 a 10: '))
    if n != r:
        print('Errou, tentei novamente')
    c += 1

print(f'Parabéns! Você acertou, eu havia pensado no nº {r}, e você precisou de {c} tentativas para adivinhar.')
