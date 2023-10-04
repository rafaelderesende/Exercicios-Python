print('-' * 10)
print('PAR OU IMPAR')
print('-'*10)
num = int(input('Digite um número qualquer: '))
div = (num % 2==0)
if div:
    print('o número {} é PAR!'.format(num))
else:
    print('O número {} é IMPAR!'.format(num))