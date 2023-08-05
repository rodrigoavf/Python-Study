# Pergunte ao usuário qual seu nome e escreva uma mensagem de boas vindas onde apareça o nome do usuário

nome = input("Qual o seu nome? ")
print('Sem usar format:')
print("É um prazer te conhecer",nome,"!")
print('Usando format:')
print("É um prazer te conhecer, {}!".format(nome))