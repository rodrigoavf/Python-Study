# Receba o nome completo de uma pessoa e retorne o primeiro e último nome separadamente

nome = str(input('Digite um nome completo: '))
print('Primeiro nome:',nome[:nome.find(' ')])
print('Último nome:',nome[nome.rfind(' ')+1:])
