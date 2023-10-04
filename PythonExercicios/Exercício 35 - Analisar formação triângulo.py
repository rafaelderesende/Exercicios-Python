reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite o valor da segund reta: '))
reta3 = float(input('Digite o valor da terceira reta: '))
if reta1 < reta2+reta3 and reta2 < reta1+reta3 and reta3 < reta1+reta2:
    print(' Os valores {}, {} e {} PODEM formar um triângulo!'. format(reta1,reta2,reta3))
else:
    print('Os valores {}, {} e {} NÃO PODEM formar um triângulo!'.format(reta1,reta2,reta3))