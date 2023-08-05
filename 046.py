'''
Apresente a contagem regrassiva para o ano novo
Com 1 segundo de espera a cada número
'''
from time import sleep
print('Faltam 10 segundooos!')
for i in range(10,0,-1):
    print(i)
    sleep(1)
print('FELIZ ANO NOVO!!!')