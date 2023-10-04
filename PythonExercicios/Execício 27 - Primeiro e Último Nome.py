n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('O primeiro nome digitado foi {}'.format(nome[0]))
print('O último nome digitado foi {}'.format(nome[len(nome)-1]))