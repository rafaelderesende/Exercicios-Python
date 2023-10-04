print('--='*10)
print('RADAR ELETRÔNICO')
print('--='*10)
Velocidade = float(input('Digite qual sua velocidade Km: '))
multa = (Velocidade - 80) * 7
if Velocidade < 80:
    print('PARABÉNS! {}Km está dentro da velocidade permitida! Faça uma boa Viagem!'.format(Velocidade))
else:
    print('ALTA VELOCIDADE! {}Km está acima da velocidade e o valor da multa é de R${:.2f}. Dirija com Segurança'.format(Velocidade,multa))