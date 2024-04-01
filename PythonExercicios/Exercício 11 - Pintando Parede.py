Largura_P = float(input('informe a largura de sua parede m: '))
Altura_P = float(input('Informe a altura de sua parede m: ' ))
LTinta = 1/2
Area_T = Largura_P * Altura_P
QTinta = LTinta*Area_T
print(' Sua área total de parede é de {:.2f}m2'.format(Area_T))
print(' Você precisará de {:.2f}lts de tinta para pintar {:.2f}m2 de parede'.format(QTinta, Area_T))