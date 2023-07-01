cont = 0
cont2 = 0
salarios = []

while cont < 11:
    salario = int(input("Digite o salário: "))
    salarios.append(salario)
    cont += 1

meses = []
meses_salario = []
maior = salarios[cont2]
while cont2 < len(salarios):
    if salarios[cont2] >= 5000:
        meses.append(cont2+1)
    if salarios[cont2] > maior:
        maior = salarios[cont2]
        meses_salario.append(cont2+1)
    cont2 += 1

meses_respostaA = []
meses_respostaB = []

def mes(x):
    if x == 1:
        return "Janeiro"
    if x == 2:
        return "Fevereiro"
    if x == 3:
        return "Março"
    if x == 4:
        return "Abril"
    if x == 5:
        return "Maio"
    if x == 6:
        return "Junho"
    if x == 7:
        return "Julho"
    if x ==8:
        return "Agosto"
    if x ==9:
        return "Setembro"
    if x == 10: 
        return "Outubro"
    if x == 11:
        return "Novembro"
    if x == 12:
        return "Dezembro"
meses_respostaA = [mes(val) for val in meses]
meses_respostaB = [mes(val) for val in meses_salario]
print("Meses com salário maior que 5000: ", meses_respostaA)
print("Meses com salário maior que o mes anteriror: ", meses_respostaB)