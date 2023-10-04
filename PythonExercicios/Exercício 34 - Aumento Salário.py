Salário = float(input(' Digite o salário do colaborador: R$  '))
Perc1 = 10/100
Perc2 = 15/100
aum1 = (Salário * Perc1) + Salário
aum2 = (Salário *Perc2) + Salário
if Salário <= 1250.00:
    print('O salário reajustado do colaboador é de R$ {}'. format(aum2))
else:
    print('O salário do colaborador reajustado é de R$ {}'.format(aum1))


