ano = int(input('Informe o ano que quer confirmar se é Bissexto ou não: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(' o Ano {} é um ano Bissexto!'.format(ano))
else:
    print(' O ano {} não é Bissexto!'.format(ano))