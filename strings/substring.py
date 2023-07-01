def substring(neandertal, tal):
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
                return indice - 1
            tam = 0
            cont = indice
            cont2 = 0
            indice += 1
    else:
        return -1