'''
TECLA'13 1ºFASE C
Emily Ribeiro

'''

n_palavras=int(input())

n_buracos=0

for linha in range(n_palavras, 0,-1):
    palavra = input().upper()
    for letra in palavra:
        if letra=='B':
            n_buracos+=2
        elif letra=='A' or letra=='D' or letra=='P' or letra=='O' or letra=='Q' or letra=='R':
            n_buracos+=1

print(n_buracos)            






