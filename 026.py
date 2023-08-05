# Receba uma frase a retorne, qtd de A, em que posição A aparece pela primeira e última vez

frase = str(input('Digite uma frase: ')).strip()
print('A frase digitada tem {} caracteres'.format(len(frase)))
print('A letra "A" aparece {} vezes'.format(frase.lower().count('a')))
print('A letra "A" aparece pela primeira vez na posição {}'.format(frase.lower().find('a')))
print('A letra "A" aparece pela última vez na posição {}'.format(frase.lower().find('a',-1)))