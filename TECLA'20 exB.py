'''
PSI - Módulo 2
TECLA'20 exB
Data: 31-10-2023
'''


M=int(input('Escreva 0 se é no ato de entrega ou 1 se for no ato de encomenda: '))
E=int(input('Escreva 0 se não for um cliente habitual ou 1 se for um cliente habitual: '))
V=float(input('Escreva o valor da encomenda'))


if(M==1):
    if(E==1):
        ValorFinal= V-0.1*V
        C=1
    else:
        ValorFinal= V-0.05*V
        C=2
else:
    if(E==0):
        ValorFinal= V+0.05*V
        C=3
    else:
        ValorFinal= V-0.1*V
        C=4

print(C ,'\n', ValorFinal)
