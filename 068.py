'''
Crie um jogo de par ou impar contra o computador
O jogo só termina quando o jogador perde
A cada jogo e ao encerrar, mostra quantas vitórias consecutivas o jogador teve
'''

from random import choice, randint

print(f'{" PAR OU IMPAR ":=^50}')
print('Vamos ver quantas vezes consectutivas você consegue me vencer!')

c = p = 0 # Número jogado pelo computador e jogador
cc = pp = '' # Escolha entre Par ou Impar do computador e do jogagor
v = 0

while True:
    cc = pp = ''
    if choice([1,2]) == 1: # Aleatório para decidir quem escolhe primeiro
        while pp not in ['P','I']:
            pp = str(input('Você começa, quer Par ou Impar? [P/I] ').upper())
            if pp not in ['P','I']: print('Opção inválida!')
        pp = "Par" if pp == "P" else "Impar"
        cc = "Impar" if pp == "Par" else "Impar"
        print(f'Você escolheu {pp}, então eu sou {cc}!')
    else:
        cc = choice(['Par','Impar'])
        pp = "Impar" if cc == "Par" else "Par"
        print(f'Eu começo, escolho {cc}, então você é {pp}')
    
    c = randint(0,10)
    p = int(input('Que número você joga? [0 a 10] '))

    print('.'*50)
    print(f'Computador: {c}')
    print(f'Jogador: {p}')
    print('.'*50)

    r = 'Par' if (c+p) % 2 == 0 else 'Impar'
    if r == cc:
        print(f'EU GANHEI! eu era {cc} e joguei {c}, {c} + {p} = {c+p} que é {r}\n')
        break
    else:
        print(f'Você venceu! você era {pp} e jogou {p}, {p} + {c} = {c+p} que é {r}')
        v += 1
        print(f'Até agora você conseguiu me vencer {v} vezes!')
    print(f'{"Próxima Rodada":-^50}\n')
print(f'{"FIM DE JOGO":-^50}')
print(f'Você conseguiu me vencer {v} vezes seguidas!\n')
