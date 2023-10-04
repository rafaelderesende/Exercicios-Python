from math import hypot
CO1 = float(input(' Digite o valor do cateto oposto de um triângulo: '))
CO2 = float(input(' Digite o valor do cateto adjacente de um trângulo: '))
HIP = hypot(CO1,CO2)
print(' O resultado do calculo entre o cateto oposto {} e o cateto adjacente {} equivale a {:.2f} correspondente ao cumprimento da hipotenusa'.format(CO1, CO2,HIP ))