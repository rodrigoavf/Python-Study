'''
Crie uma tupla com números de 0 a 20 em extenso
Receba um número do usuário entre 0 e 20 e retorne este número por extenso
'''

numeros_extenso = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
    'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
)
while True:
    n = int(input('Digite um número de 0 a 20: [-1 pra encerrar] '))
    if n == -1: 
        break
    elif  n < -1 or n > 20:
        print('Número inválido')
    else:
        print(numeros_extenso[n])
