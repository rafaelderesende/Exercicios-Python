Celsius = float(input('Digite a temperatura em graus ºC: '))
F_Conversao = (9/5)
Ref_Fahrenheit = 32
Fahrenheit = (Celsius * F_Conversao)+Ref_Fahrenheit
Kelvin = Celsius+273.15
print('A temperatura convertida de {}ºC é {}ºF e {}ºK '.format(Celsius,Fahrenheit,Kelvin))