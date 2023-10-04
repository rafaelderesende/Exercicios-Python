carro = int(input('Digite quantos anos possui seu carro: '))
if carro <5:
    print('Seu carro é considerado semi-novo!')
else:
    print('Seu carro é considerado antigo! ')
print('________FIM________')

N1 = float(input('Digite a primeira nota do aluno: '))
N2 = float(input('Digite a segunda nota do aluno: '))
média = (N1 + N2)/2
if média >= 6:
    print('Considerando a primeira nota {} e a segunda {}, a média do aluno é {}. Aluno APROVADO!'.format(N1,N2,média))
else:
    print('Considerando a primeira nota {} e a segunda {}, a média do aluno é {}. Aluno REPROVADO!'.format(N1,N2,média))

