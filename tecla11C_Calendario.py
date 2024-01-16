'''
Emily Ribeiro
PSI - Módulo 3
Tecla 11 - ex C
Mostrar Calendario
12-12-23
'''
'''
import calendar
ano = int(input("Digite o ano: "))
mes = int(input("Digite o mês (entre 1 e 12): "))
print(calendar.month(ano, mes))
'''

def imprimir_calendario(m, a, d):
    # Dicionário para mapear números de dias da semana para nomes
    dias_semana = {1: 'Dom', 2: 'Seg', 3: 'Ter', 4: 'Qua', 5: 'Qui', 6: 'Sex', 7: 'Sab'}

    # Lista com a quantidade de dias em cada mês
    dias_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Imprime o cabeçalho com o mês e o ano
    print(f"{m:02d}-{a}")
    print(" ".join(dias_semana.values()))

    # Imprime os espaços em branco até o primeiro dia da semana
    print("   " * (d - 1), end="")

    # Imprime os dias do mês
    for i in range(1, dias_mes[m] + 1):
        print(f"{i:02d}", end=" ")
        if (i + d - 1) % 7 == 0:
            print()  # Pula para a próxima linha a cada sete dias

print(imprimir_calendario(1,2010,6))



