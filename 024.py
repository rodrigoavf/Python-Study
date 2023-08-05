# Receba o nome de uma cidade e identifica se ela começa com a palavra SANTO ou não

cidade = str(input('Informe o nome da cidade: ')).strip()
print('Cidade começa com Santo?\n{}'.format(cidade.lower().startswith('santo')))