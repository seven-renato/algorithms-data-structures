def questao1(nomeArq,numCanal:int):
    arq = open(f"{nomeArq}.txt","r")
    lista = arq.readlines()
    arq.close()
    vet = []
    for val in lista:
        vet.append(val[:-1].split(";"))
    total = 0
    audiencia = 0
    for val in vet:
        total += int(val[1])
        if val[0] == str(numCanal):
            audiencia += int(val[1])
    return f"{(100 * audiencia)/total} %"


print(questao1("canais",4))
print(questao1("canais",5))
print(questao1("canais",7))
print(questao1("canais",12))