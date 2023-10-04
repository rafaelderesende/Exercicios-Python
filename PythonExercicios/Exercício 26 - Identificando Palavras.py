frase = str(input('Digite uma frase: ')).upper().strip()
print(' A letra A aparece nesta frase {} vezes'.format(frase.count('A')))
print('A primeira letra A aparece na posição {}'.format(frase.find('A')))
print(' A última posição da letra aparece na posição {}'.format(frase.rfind('A')))