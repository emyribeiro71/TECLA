num=int(input(''))
primo = True 


if num==1:
    print('0')
else:
    for i in range(2,num):
        divisao = num % i
        if divisao == 0 :
            primo = False
            break
    if primo:
        print('1')
    else:
        print('0')
