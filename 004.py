# Peça um input qualquer ao usuário e traga informações sobre este input

algo = input('Digite algo : ')
print('Informações sobre o input fornecido:')
print('O tipo do input é {}'.format(type(algo)))
if algo.isdecimal() == True:
    decimal=' '
else:
    decimal=' não '
print('O input{}é um decimal'.format(decimal))
if algo.isalpha() == True:
    alpha=' '
else:
    alpha=' não '
print('O input{}é alfabético'.format(alpha))
if algo.isalnum() == True:
    alphanum=' '
else:
    alphanum=' não '
print('O input{}é alfanumérico'.format(alpha))
if algo.isnumeric() == True:
    num=' '
else:
    num=' não '
print('O input{}é numérico'.format(alpha))