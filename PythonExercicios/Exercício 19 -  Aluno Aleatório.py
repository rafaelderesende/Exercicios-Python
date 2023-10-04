from random import  choice
Aluno_1 = str(input('Digite o primeiro aluno: '))
Aluno_2 = str(input('Digite o primeiro aluno: '))
Aluno_3 = str(input('Digite o primeiro aluno: '))
Aluno_4 = str(input('Digite o primeiro aluno: '))
lista = [Aluno_1,Aluno_2,Aluno_3,Aluno_4]
Escolhido = choice(lista)
print('O Aluno escolhido foi {}'.format(Escolhido))



