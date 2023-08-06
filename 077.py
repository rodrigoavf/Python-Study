'''
Crie uma tupla com várias palavras
Para cada palavra mostrar quais são as vogais
'''

vogais = ('a','e','i','o','u')
palavras = ("abacaxi", "banana", "cenoura", "dado", "elefante", "flor", "girafa", "helicoptero", "igreja", "janela")

for p in palavras:
    print(f'\nEm {p} temos as vogais: ',end='\n')
    for l in p:
        if l.lower() in vogais:
            print(f'{l.lower()} ',end=' ')
l