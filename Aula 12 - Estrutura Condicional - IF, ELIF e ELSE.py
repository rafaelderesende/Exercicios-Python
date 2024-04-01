nome = str(input('Digite Seu Nome: '))
if nome == 'Rafael':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Paulo' or nome == 'Maria':
    print('É um nome muito popular aqui no Brasil!')
elif nome in 'Ana' or 'Polliana' or 'Priscilla':
    print('Belo nome feminino!')
else:
    print('Legal!')
print('Tenha um bom dia, {}!'.format(nome))