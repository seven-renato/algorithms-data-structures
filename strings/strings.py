nome = "Paulo"
"""print(nome[0])
print(nome[1])
print(nome[2])
print(nome[4])
print(nome[3])"""

x = "Cadeira"
for letra in x:
    print("--->",letra)

vogais = list("aáàeéèiìíoóòuúù")

cont2 = 0
nome = ("Paulo Renato Pereira das Neves Neto").lower()
for letras in nome:
    if letras in vogais:
        cont2 += 1
print(cont2)

def espelho_meu(nome_int):
    cont = len(nome_int)-1
    nome = []
    while cont >= 0:
        nome.append(nome_int[cont])
        cont -= 1
    return "".join(nome)
def espelho(nome):
    x = ""
    cont = len(nome)-1
    while cont >= 0:
        x += nome[cont]
        cont -= 1
    return x
print(espelho("Paulo"))

def substring(neandertal,tal):
    string = neandertal.lower()
    substring = tal.lower()
    test = False
    tam = 0
    cont = 0
    indice = 0
    cont2 = 0
    if substring in string:
        while indice < len(string):
            while tam < len(substring):
                if string[cont] == substring[cont2]:
                    test = True
                    cont += 1
                    cont2 += 1
                else:
                    tam = len(substring)
                    test = False
                tam += 1
            if indice == 0 and test:
                return indice
            elif test:
                return indice-1
            tam = 0
            cont = indice
            cont2 = 0
            indice += 1
    else:
        return -1
    

print(substring("neandertal","tal"))
print(substring("gato","to"))
print(substring("chocolate","cho"))
print(substring("paralelepipedo","ped"))

