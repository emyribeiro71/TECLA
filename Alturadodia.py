horas=int(input(''))
if horas>=5 and horas<=7:
    print('madrugada')
elif horas>=8 and horas<=12:
    print('manha')
elif horas>=13 and horas<=19:
    print('tarde')
else:
    print('noite')
