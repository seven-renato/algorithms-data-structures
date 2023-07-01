cont = 0
notas = []
media = 0
while cont < 10:
    nota = float(input("Insira uma nota: "))
    notas.append(nota)
    if cont == 0:
        maior = nota
    cont += 1
    if nota > maior:
        maior = nota
    media += nota
print("Maior nota =",max(notas))
print("Maior", maior)
print("Media =",(media/cont))
print("Media 2 =", sum(notas)/len(notas))