'''
Receba vários números inteiros
O programa só para quando receber 999
Ao final, mostrar:
- A soma entre todos
- Quantos números foram digitados
'''

l = []
while True:
    n = int(input('Insira quando números quiser, uma a um [999 para encerra]: '))
    if n == 999: break
    l.append(n)
print(f'A soma entre os {len(l)} número informados é {sum(l)}')
