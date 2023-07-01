arq1 = open("curso1.txt","r", encoding="utf-8")
lista1 = arq1.readlines()
arq1.close()
arq2 = open("curso2.txt","r",encoding="utf-8")
lista2 = arq2.readlines()
arq2.close()
arq3 = open("curso3.txt","r",encoding="utf-8")
lista3 = arq3.readlines()
arq3.close()

def tratamentoDosDados(array):
    vet = [] 
    for val in array:
        vet.append(val[:-1])
    vetor = []
    matrix_aux = []
    for val in vet:
        vetor.append(val.split("; "))

    return vetor

curso1 = tratamentoDosDados(lista1)
curso2 = tratamentoDosDados(lista2)
curso3 = tratamentoDosDados(lista3)
totalCursos = [curso1,curso2,curso3]
totalDeCandidatos = 0
for val in totalCursos:
    totalDeCandidatos += int(val[3][1])
    totalDeCandidatos += int(val[4][1])
print("O total de candidatos foi",totalDeCandidatos,".")
#Total de candidatos

vet = []
vet_aux = []
totalCandidatosCurso = 0
for val in totalCursos:
    totalCandidatosCurso += int(val[3][1])
    totalCandidatosCurso += int(val[4][1])
    vet_aux.append(round(totalCandidatosCurso/int(val[2][1]),2))
    vet_aux.append(round(int(val[4][1])/totalCandidatosCurso*100,2))
    vet_aux.append(val[1][1])
    totalCandidatosCurso = 0
    vet.append(vet_aux)
    vet_aux = []
print(vet) #Candidatos p/ Vaga, %Feminina, Codigo correspondente do curso

maior = 0
for val in vet:
    if val[0] > maior:
        maior = val[0]
cont = 0
for val in vet:
    if val[0] == maior:
        break
    cont += 1

print(f"O maior número de candidatos por vagas é {maior} pessoas por vaga, o curso que possui esse valor se trata do {vet[cont][2]}.")