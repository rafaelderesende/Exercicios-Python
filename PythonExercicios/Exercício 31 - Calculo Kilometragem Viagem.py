print('-=' * 15)
print('RAFA RENT CAR')
print('-=' * 15)
Distância = float(input(' Por favor informe a distância percorrida em km: '))
V1 = Distância * 0.50
V2 = Distância * 0.45
if Distância < 200:
    print(' A distância informada foi {}Km e o valor a pagar é de R$ {:.2f}'.format(Distância,V1))
else:
    print(' A distância informada foi {}Km e o valor a pagar é de R$ {}'.format(Distância,V2))
print(' VOLTE SEMPRE! RAFA RENT CAR AGRADECE A PREFERÊNCIA!')