'''
PSI - Módulo 2
TECLA'22 exB
Data: 31-10-2023
'''


#input

P=float(input('Qual é o valor da sapatilha?'))
C=str(input('Tem um cupom? ')).lower()

if(C=='sim'):
    Vc=float(input('Qual é o valor do seu cupom?'))
    P -= Vc

entrega=str(input('Como deseja receber a sua encomenda? Na loja ou CTT?')).lower()
#verificar se tem porte ou não
if(entrega=='ctt' and P<=50):
    P+= 3.95

print(P)

















    


