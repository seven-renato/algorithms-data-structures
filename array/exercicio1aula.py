cont = 0
notas = []
while cont < 3:
    nota = float(input("Insira uma nota: "))
    notas.append(nota)
    cont +=1

"""cont2 = 0
while cont != 0:
    print("notasinvertida[{}] = {}".format(cont2,notas[cont-1]))
    cont2 += 1
    cont -=1"""


#ou
notasinvertida = []
cont = cont -1
while cont >= 0:
    notasinvertida.append(notas[cont])
    cont -= 1
print("---",notasinvertida)

cont2 =  0
while cont2 < (len(notas)):
    if notas[cont2] >= 7:
        print("Indices com nota maior que 7, notas[{}] = {}".format(cont2,notas[cont2]))
    cont2 += 1