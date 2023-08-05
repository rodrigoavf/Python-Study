# \33[style;text;backgroundm
print('\n')  # pula linha

print("OPÇÕES DE STYLE [0, 1, 4, 7]")
# O \033[m no final resata o style para o padrão, caso contrário ele continuaria com a formatação para o próximo print combinando com a outra nova formatção
print('\033[0mStyle = 0 = Sem style\033[m')
print('\033[1mStyle = 1 = Negrito\033[m')
print('\033[4mStyle = 4 = Sublinhado\033[m')
print('\033[7mStyle = 7 = Negativo\033[m')
print('\033[1m\033[4m\033[7mTodos juntos\033[m')

print('\n')  # pula linha

print("OPÇÕES DE TEXT [30, 31, 32 ,33, 34, 35, 36, 37]")
print('\033[30mText = 30 = Cinza')
print('\033[31mText = 31 = Vermelho')
print('\033[32mText = 32 = Verde')
print('\033[33mText = 33 = Amarelo')
print('\033[34mText = 34 = Azul')
print('\033[35mText = 35 = Magento')
print('\033[36mText = 36 = Ciano')
print('\033[37mText = 37 = Branco')

print('\n')  # pula linha

print("OPÇÕES DE BACKGROUND [40, 41, 42 ,43, 44, 45, 46, 47]")
print('\033[40mBackground = 40 = Cinza\033[m')
print('\033[41mBackground = 41 = Vermelho\033[m')
print('\033[42mBackground = 42 = Verde\033[m')
print('\033[43mBackground = 43 = Amarelo\033[m')
print('\033[44mBackground = 44 = Azul\033[m')
print('\033[45mBackground = 45 = Magento\033[m')
print('\033[46mBackground = 46 = Ciano\033[m')
print('\033[47mBackground = 47 = Branco\033[m')

print('\n')  # pula linha
