Valor_Cateira = float(input(' Digite o valor que você possui neste momento em R$: '))
TxC = float(input('Digite a cotação do Dólar Americano (U$): '))
Conversão = Valor_Cateira/TxC
print('-'*35)
print('RESULTADO DA CONVERSÃO EM U$')
print('Você possui neste momento U$ {:.2f}'.format(Conversão))
print('-'*35)