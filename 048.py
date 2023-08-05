'''
Calcula a some entre todos os números ímpares
que são múltiplos de 3 e que estão no intervalo entre 1 e 500
'''
n = c = 0 # Declaração de 2 variáveis ao mesmo tempo
for i in range(1,501,3): # Pula de 3 em 3
    if i % 2 == 1: # Verifica se é ímpar
        n += i 
        c += 1
        print(i, end = ' ')
print('\n')
print(f'A soma de todos os {c} números ímpares e múltiplos de 3 no intervado 1-500 é:{n}')
