'''
Crie um jogo de jokenpô contra o pc
'''

import random

c = random.randint(1,3)
print('Vamos jogar Jokenpô, o que você escolhe?')
p = int(input('''
Escolha uma das opções:
1 = Pedra
2 = Papel
3 = Tesoura
'''))
i = ('Pedra', 'Papel', 'Tesoura')
match c:
    case 1:
        print('Computador = {}'.format(i[c-1]))
    case 2:
        print('Computador = {}'.format(i[c-1]))
    case 3:
        print('Computador = {}'.format(i[c-1]))
match p:
    case 1:
        print('Jogador = {}'.format(i[p-1]))
    case 2:
        print('Jogador = {}'.format(i[p-1]))
    case 3:
        print('Jogador = {}'.format(i[p-1]))

if c == 1 and p == 2:
    print('Você ganhou, papel vence pedra')
elif c == 1 and p == 3:
    print('Eu ganhei! Pedra ganha de tesoura!')
elif c == 2 and p == 3:
    print('Você ganhou, papel perde de tesoura')
elif c == 2 and p == 1:
    print('Eu ganhei! papel ganha de pedra')
elif c == 3 and p == 1:
    print('Você ganho, pedra ganha de tesoura')
elif c == 3 and p == 2:
    print('Eu ganhei! Tesoura ganha de papel')
else:
    print('Ninguém ganhou, nós dois escolhemos a mesma coisa')