# Insira duas notas de um aluno e calcule a média

n1 = float(input('Nota 1 do aluno: '))
n2 = float(input('Nota 2 do aluno: '))

#Posso fazer o cálculo simples de média manualmente
avg_simples = (n1+n2)/2
print("A média calculada manualmente entre {} e {} é: {}".format(n1, n2, avg_simples))

#Posso definir uma função que calcula a média entre dois números
def media(num1, num2):
    return(num1 + num2)/2

avg_def = media(n1, n2)
print('A média calculada por uma função definida pelo usuário entre {} e {} é: {}'.format(n1, n2, avg_def))

#Posso importar uma biblioteca que contém uma função de média
import statistics as st
notas = [n1,n2] #necessário criar uma lista pois a função mean só tem 1 parâmetro
avg_biblioteca = st.mean(notas)
print('A média calculada usando a biblioteca statistics entre {} e {} é: {}'.format(n1, n2, avg_biblioteca))