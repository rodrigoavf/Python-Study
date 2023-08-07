'''
Simule um caixa eletrônico
- O saldo inicial da pessoa será um número aleatório entre 100 e 1000
- O caixa só pussui células de 100, 50, 20 e 10
'''

from random import randint
import pandas as pd

extrato = pd.DataFrame(columns=['Movimentação','Valor'])
saldoInicial = saldo = randint(100,10000)

print(f'{" CAIXA ELETRÔNICO - DIDIGO BANK ":=^50}')
while True:
    depósito = -1
    saque = 1.1
    i = -1

    print('.'*50)
    print('[0] Saldo')
    print('[1] Saque')
    print('[2] Depósito')
    print('[3] Extrato')
    print('[9] Sair')
    print('.'*30)
    while i not in [0,1,2,3,9]:
        i = int(input('Digite uma opção: '))

    match i:
        case 0: # Saldo
            print(f'Seu saldo atual é de: R${saldo:,.2f}')
        case 1: # Saque
            print('Notas disponíveis: [100, 50, 20, 10]')
            while saque % 10 != 0:
                saque = int(input('Qual valor deseja sacar? R$'))
                if saque % 10 != 0:
                    print('Valor inválido! Digite um valor múltiplo de 10, sem os centavos')
            saldo -= saque
            extrato.loc[len(extrato)] = ['Saque', -saque]

            notas100 = int(saque/100)
            notas50 = int((saque-notas100*100)/50)
            notas20 = int((saque-notas100*100-notas50*50)/20)
            notas10 = int((saque-notas100*100-notas50*50-notas20*20)/10)
            
            print('Você receberá seu saque em:')
            for i in [[notas100,100],[notas50,50],[notas20,20],[notas10,10]]:
                if i[0] > 0: print(f'{i[0]} notas de R${i[1]}')
            #Método alternativo:
            #if notas100 > 0: print(f'{notas100} notas de R$100')
            #if notas50 > 0: print(f'{notas50} notas de R$50')
            #if notas20 > 0: print(f'{notas20} notas de R$20')
            #if notas10 > 0: print(f'{notas10} notas de R$10')

            print('Saque efetuado com sucesso!')
        case 2: # Depósito
            while not isinstance(depósito, int) or depósito < 0:
                depósito = input('Qual valor deseja depositar? R$')
                if not depósito.isdigit(): 
                    print('Este não é um valor válido, informe um valor numérico sem centavos.')
                else:
                    depósito = int(depósito)
            saldo += depósito
            extrato.loc[len(extrato)] = ['Depósito', depósito]
            print('Depósito efetuado com sucesso!')
        case 3: # Extrato
            if len(extrato) > 0:
                print(f'Saldo inicial: R${saldoInicial:,.2f}')
                print(extrato)
                print(f'Saldo atual: R${saldo:,.2f}')
            else:
                print('Não existe nenhuma movimentação recente')
    
    print('.'*30)
    if i == 9: break
print('.'*50)
print(f'{" OPERAÇÃO ENCERRADA ":=^50}'+'\n')
