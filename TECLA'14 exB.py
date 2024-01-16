'''
PSI - Módulo 2
TECLA'14 exB
Data: 31-10-2023
'''


V=float(input('incira o valor a converter: '))
U=str(input('Qual é a unidade do valor? '))

Polegada = 'in'
Pe = 'ft'
jarda= 'yd'
milha= 'mi'


if(U=='in'):
    Cm=V*2.54
elif(U=='ft'):
    Cm=V*30.48
elif(U=='yd'):
    Cm=V*91.44
elif(U=='mi'):
    Cm==V*160000

print(Cm)









