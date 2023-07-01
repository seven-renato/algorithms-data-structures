def questao7():
    def uppercase(string):
        if ord(string) >= 97 and ord(string) <= 122:
            x = ord(string) - 32
            return chr(x)
        else:
            return string

    def upper(frase):
        palavra_fim = ""
        for letra in frase:
            palavra_fim += uppercase(letra)
        return (palavra_fim)

    def invertexto(string):
        no_spc = ""
        for i in string:
            if i == " ":
                pass
            else:
                no_spc += i
        no_spc = upper(no_spc)
        texto_inv = ""
        cont = len(no_spc)-1
        while cont >= 0:
            texto_inv += no_spc[cont]
            cont -= 1
        if no_spc == texto_inv:
            return True
        else:
            return False

    print(invertexto("Mirim"))


def questao8_space(string):
    sem = ""
    cont = 0
    for letra in string:
        if letra == " ":
            cont += 1
        else:
            if cont > 0:
                sem += " "
                sem += letra
                cont = 0
            else:
                sem += letra
    return(sem)

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
    cont, cont2 = 0, 0, 0
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

def questao9():
    fr1 = "O Gremio é o melhor time Gremio"
    fr2 = "Gremio"
    fr3 = "Real Madrid"
    print(join(split(fr1,fr2),fr3))

def multiplicar_matriz():
    m1 = [[1, 2], [2, 4]]
    m2 = [[1, 2, 3], [2, 4, 5]]
    #m2 = [[1,2,3],[2,4,5]]

    if len(m1[0]) == len(m2):
        print("Dá")
    else:
        print("Não dá")

