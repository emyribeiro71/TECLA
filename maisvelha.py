Joana = int(input(''))
Monica  = int(input(''))
Sofia = int(input(''))

maior = Joana
if (Monica > maior):
    maior = Monica
if (Sofia < Monica):
    maior = Joana

print(maior)