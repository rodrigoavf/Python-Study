'''
Receba vários números inteiros
Pare de aceitar números quando 999 for inserido
No final, desconsiderando 999, mostre:
- Quantos números foram informado
- A soma dos números
'''

l = []
while True:
    n = int(input('Insira quando números quiser, uma a um [999 para encerra]: '))
    if n == 999: break
    l.append(n)
print(f'A soma entre os {len(l)} número informados é {sum(l)}')
