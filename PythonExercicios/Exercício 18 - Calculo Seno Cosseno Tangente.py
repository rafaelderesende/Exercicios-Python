from math import radians, sin,cos,tan
Angulo = float(input(' Digite um ângulo de um circulo trigonométrico: '))
Seno = sin(radians(Angulo))
Cosseno = cos(radians(Angulo))
Tangente = tan(radians(Angulo))
print(' Dado o ângulo de {} graus em questão, temos o Seno {:.2f}, Cosseno {:.2f} e Tangente {:.2f}'.format(Angulo,Seno, Cosseno,Tangente))
