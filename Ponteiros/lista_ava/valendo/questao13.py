import math
from datetime import *
def QuantosDias(dia, mes, ano):
    if dia > 31 or dia < 1  or ano < 2022 or mes > 12 or mes < 1:
        return
    elif mes == 2 and dia > 28:
        return
    diasPorMes = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    anoAtual = date.today().year
    diaAtual = date.today().day
    mesAtual = date.today().month
    totalDeDias = diasPorMes[mesAtual-1] - diaAtual + dia# Dias restantes no mes atual
    if ano == anoAtual:
        for i in range(mesAtual,mes-1):
            totalDeDias += diasPorMes[i]
        return totalDeDias
    else:
        for i in range(mesAtual,len(diasPorMes)):
            totalDeDias += diasPorMes[i]
    #total de dias até o fim do ano
    for i in range(1, ano-anoAtual):
        if i % 4 == 0:
            totalDeDias += 366
            teste = True
        else:
            totalDeDias += 365
    if teste:
        totalDeDias += 1
    for i in range(mes-1):
        totalDeDias += diasPorMes[i]
    return totalDeDias  

print(QuantosDias(28,2,2069))























