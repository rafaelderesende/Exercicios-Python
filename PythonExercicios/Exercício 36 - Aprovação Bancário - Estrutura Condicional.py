print('-*-' * 15)
print(' BEM VINDO AO RAFAs BANK')
print('CRÉDITO RÁPIDO, FÁCIL E SEM BUROCRCIA')
print('-*-' * 15)

#Questionário para o Comprador
Valor_Casa = float(input('Digite o valor desejado para o imóvel dos seus sonhos R$: '))
Salario = float(input('Digite sua renda mensal bruta em R$: '))
Prazo = int(input('Em quantos anos você pretende pagar este o imóvel dos seus sonhos: '))

# Cálculo de parcelas e prazos
Parcela_Cliente = Salario / 100 * 30
Apr_Ngt = (Valor_Casa / Prazo) / 12
if Parcela_Cliente >= Apr_Ngt:
    print('O valor mínimo exigido para credito neste valor é de R$ {:.2f}. Com base em seu salário, sua renda consegue pagar parcelas mensais de até R$ {:.2f}, o que  cobre o valor mínimo exigido. Seu Crédito foi APROVADO! Parabéns.'.format(Apr_Ngt,Parcela_Cliente))
else:
    print('O valor mínimo exigido para credito neste valor é de R$ {:.2f}.Com base em seu salário, sua renda consegue pagar parcelas mensais de até R$ {:.2f}. Seu Crédito infelizmente foi Negado. Esperamos poder ajudar em uma próxima oportunidade.'.format(Apr_Ngt,Parcela_Cliente))

print('-*-' * 15)
print(' AGRADECEMOS EM NOME DO RAFAs BANK')
print('CRÉDITO RÁPIDO, FÁCIL E SEM BUROCRCIA')
print('-*-' * 15)



