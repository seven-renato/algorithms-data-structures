arq = open("temperaturas.txt","r")
lista = arq.readlines()
arq.close()
vet = []
for val in lista:
    vet.append(float(val[:-1]))

mediaAnual = sum(vet)/len(vet)
meses = ["Janeiro","Fevereiro","Março","Abril","Maior","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
vetor = []
cont = 0
sup = []
for val in vet:
    if val > mediaAnual:
        sup.append(val)
        sup.append(cont)
        vetor.append(sup)
    sup = []
    cont += 1

word = f"Media anual {mediaAnual:.2f}°C\n"

for val in vetor:
    word += f"{val[1]+1} - {meses[val[1]]} - {val[0]}°C\n"
print(word)