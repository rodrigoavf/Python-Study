'''
Crie uma tuple com 20 times de futebol e exiba:
- Apenas os 5 primeiros
- Os últimos 4
- A lista completa em ordem alfabética
- Em que posição na tabela está o São Paulo
'''

times = (
    "Flamengo",
    "Internacional",
    "Atlético Mineiro",
    "São Paulo",
    "Fluminense",
    "Grêmio",
    "Palmeiras",
    "Santos",
    "Athletico Paranaense",
    "Red Bull Bragantino",
    "Ceará",
    "Corinthians",
    "Atlético Goianiense",
    "Bahia",
    "Sport Recife",
    "Fortaleza",
    "Vasco da Gama",
    "Goiás",
    "Coritiba",
    "Botafogo"
)

print('Os 5 primeiros')
print('-'*50)
print(times[:4])
print('-'*50+'\n')

print('Os 4 últimos')
print('-'*50)
print(times[-4:])
print('-'*50+'\n')

print('Em ordem alfabética')
print('-'*50)
print(sorted(times))
print('-'*50+'\n')

print('Posição do São Paulo')
print('-'*50)
print(times.index('São Paulo')+1)
print('-'*50+'\n')