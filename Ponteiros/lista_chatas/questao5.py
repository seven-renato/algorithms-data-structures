arq = open("./usuarios.txt","r")
lista = arq.readlines()
arq.close()

def formatar_arq(array):
    vet = []
    for val in array:
        vet.append(val[:-1].split(" "))
    return vet

def converterMB(num):
    num = int(num)
    return round(num/(1024**2),2)

def percentual(num,total):
    return round((100*num)/total,2)

vet = formatar_arq(lista)



vetor = []
for val in vet:
    lista = []
    lista.append(val[0])
    lista.append(converterMB(val[1]))
    vetor.append(lista)

total = 0 
for val in vetor:
    total += val[1]
media = total/len(vetor)

word = ""
word += "Furg       Uso do espaço em disco pelos usuários\n"+"--"*24
word += "\nNr. Usuário       Espaço utilizado    % do uso\n\n"
cont = 1
for val in vetor:
    word += f"{cont} {val[0]:<15} {val[1]:<6} MB {percentual(val[1],total):>17}%\n"
    cont += 1
word += f"\n\nEspaço total ocupado: {total:.2f} MB"
word += f"\nEspaço médio ocupado: {media:.2f} MB"

print(word)