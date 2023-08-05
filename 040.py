'''
Receba duas notas de um aluno e calcule a média
Mostre uma das mensagens:
- Média abaixo de 5.0 = Reprovado
- Média entre 5.0 e 6.9 = Recuperação
- Média 7.0 ou maior = Aprovado
'''
from statistics import mean
n1 = float(input('1ª nota do aluno: '))
n2 = float(input('2ª nota do aluno: '))
avg = mean([n1,n2])

print('Média =',avg)
if avg < 5.0:
    print('Média abaixo de 5.0 = Reprovado')
elif avg < 6.9:
    print('Média entre 5.0 e 6.9 = Recuperação')
else:
    print('Média 7.0 ou maior = Aprovado')