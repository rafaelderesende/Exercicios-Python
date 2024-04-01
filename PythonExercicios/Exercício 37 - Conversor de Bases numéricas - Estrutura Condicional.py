num = int(input('Digite um número inteiro: '))
print(''' Escolha uma das bases de conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
Opção = int(input('Sua Opção: '))
if Opção == 1:
    print('{} convertido para BINÁRIO é igual á {}'.format(num, bin(num)))
elif Opção == 2:
    print('{} convertido para OCTAL é igual á {}: '.format(num, oct(num)))
elif Opção == 3:
    print('{} convertido para HEXADECIMAL é igual á {}'.format(num,hex(num)))
