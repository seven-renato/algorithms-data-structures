def split(string, separador):
    word = ""
    array = []
    if type(separador) == int:
        return("TypeError: must be str or None, not int")
    elif separador not in string:
        array.append(string)
        return array
    elif separador == "":
        return "ValueError: empty separator"
    cont, cont2, cont4 = 0, 0, 0
    teste = False
    error = False
    while cont < len(string):
        if string[cont] != separador[0]:
            word += string[cont]
        else:
            while True and error == False:
                if cont2 == len(separador):
                    teste = True
                    array.append(word)
                    word = ""
                    break
                if string[cont] != separador[cont2]:
                    error = True
                if string[cont] == separador[cont2]:
                    cont += 1
                    cont2 += 1
        if teste:
            cont -= 1
        if error:
            word += string[cont-1]
            cont -= 1
        error = False
        teste = False
        cont += 1
        cont2 = 0
    if len(word) >= 0:
        array.append(word)
    return array


def join(array, join):
    word = ""
    cont = 0
    if len(array) == 0:
        return(None)
    if len(array) > 1:
        for i in array:
            cont += 1
            if cont == len(array):
                word += i
            else:
                word += i + join
    else:
        if join == "":        
            word += array[0]
    return word


string1 = "barro"
string2 = "doces"

arq1 = open(
    "C:\\Users\\seven\\Documents\\Projetos\\FURG\\AULA\\algortimo\\strings\\questao10-1.txt", "r")
read = arq1.readlines()
arq1.close

arq2 = open(
    "C:\\Users\\seven\\Documents\\Projetos\\FURG\\AULA\\algortimo\\strings\\questao10-2.txt", "r+")

word = ""
for letter in read:
    word += letter

a = join(split(word, string1),string2)
arq2.write(f"{a}\n")
leitura = arq2.readlines()
print(join(leitura,""))
arq2.close