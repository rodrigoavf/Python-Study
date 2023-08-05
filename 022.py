# Receba um nome completo e traga, tudo em maiúsculo, minúsculo, a quantidade de caracteres, e a qtd de caracteres no primeiro nome

nome = str(input('Insira um nome completo: '))
print('Tudo maisúculo:', nome.upper())
print('Tudo minúsculo:', nome.lower())
print('Qtd de caracteres:', len(nome))
print('Qtd de caracteres sem contar espaços:', len(nome.replace(' ','')))
pnome = nome[:nome.find(' ')]
print('O primeiro nome é:',pnome)
print('Qtd de caracteres no primeiro nome',len(pnome))