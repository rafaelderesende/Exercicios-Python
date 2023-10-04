from random import choice
lista = [0,1,2,3,4,5]
print('--+'*12)
print('JOGO DA ADIVINHAÇÃO')
print('--+'*12)
usu = int(input('Jogo da adivinhação: Digite um número entre 0 e 5 para tentar adivinhar qual número o computador escolheu: '))
pc_num = choice(lista)
print('O número escolhido pelo computador foi {}'.format(pc_num))
if pc_num == usu:
    print('PARABÉNS! O número {} é o mesmo que o computador!'.format(usu) )
else:
    print('QUE PENA!. O número {} não é o mesmo que você escolheu {}'. format(pc_num,usu))