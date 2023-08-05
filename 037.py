'''
Receba um número inteiro e peça ao usuário escolher a base
de conversão sendo:
1 = binário
2 = octal
3 = hexadecimal
'''

n = int(input('Insira um valor inteiro a ser convertido: '))
i = int(input(
'Para qual base deseja converte o número?\n'
'Digite:\n'
'1 = binário\n'
'2 = octal\n'
'3 = hexa\n'
))

if i == 1:
    print(bin(n)[2:])
elif i == 2:
    print(oct(n)[2:])
else: 
    print(hex(n)[2:])