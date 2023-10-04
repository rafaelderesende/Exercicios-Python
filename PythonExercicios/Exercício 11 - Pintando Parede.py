Largura_P = float(input('informe a largura de sua parede m: '))
Altura_P = float(input('Informe a altura de sua parede m: ' ))
LTinta = 1/2
Area_T = Largura_P * Altura_P
QTinta = LTinta*Area_T
print(' Sua área total de parede é de {}m2'.format(Area_T))
print(' Você precisará de {}lts de tinta para pintar {}m2 de parede'.format(QTinta, Area_T))