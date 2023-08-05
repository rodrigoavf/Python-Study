'''
Receba uma frase e diga se ela é um palíndromo
Ou seja que pode ser lida igual de trás pra frente
'''
from unidecode import unidecode

def remove_graphic_accents(string):
    return unidecode(string)

f = str(input('Insira uma frase qualquer: '))
f_semacentos = remove_graphic_accents(f)
f_semespaco = f_semacentos.replace(' ','')
f_reverso = f_semespaco[::-1]

print(f'Tirando os acentos, fica: {f_semacentos}')
print(f'Tirando os espaços, fica: {f_semespaco}')
print(f'Revertendo, fica: {f_reverso}')
print('Sendo assim...')
if f_semespaco == f_reverso:
    print(f'A frase "{f}" é um palíndromo')
else:
    print(f'A frase "{f}" não é um palíndromo')
