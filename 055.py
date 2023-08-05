'''
Receba o peso de 5 pessoas
Mostre quem é o mais leve e o mais pesado
'''
lp = []
for i in range(0,5):
    p = float(input(f'Qual o peso da {i+1}ª pessoa: '))
    lp.append(p)

print(f'A {lp.index(max(lp))+1}ª pessoa é a mais pesada com {max(lp)}kg e a {lp.index(min(lp))+1}ª é a mais leve com {min(lp)}kg')
