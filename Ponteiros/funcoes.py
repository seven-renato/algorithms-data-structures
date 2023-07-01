def minhaFuncMax(array):
    maior = array[0]
    for val in array:
        if val > maior:
            maior = val
    return maior

def minhaFuncMin(array):
    menor = array[0]
    for val in array:
        if val < menor:
            menor = val
    return menor


def minhaFuncSum(array):
    soma = 0
    for val in array:
        soma += val
    return soma         


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

def sortMeu(array):
    cont = 0 
    cont2 = 0
    menor = min(array)
    while True:
        if cont2 == len(array)-1:
            break
        if array[cont] <= menor:
            teste = array[cont]
            array[cont] = array[cont2]
            array[cont2] = teste
            cont2 += 1
            cont = cont2 - 1
        menor = min(array[cont2:])
        cont += 1
    return array

def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    return fibo(x-1) + fibo(x-2)
print(fibo(6))

def eh_primo(x):
    cont = 2
    if x % 2 == 0:
        return("N")
    if x == 1 or x == 2:
        return ("S")
    while cont < (x/2):
        if x % cont == 0:
            return ("N")
        cont = cont + 1
    return("S")


def squareRoot2(n): 
    if n == 0: 
        return 2 
    x = 2+1/squareRoot2(n-1) # a recursividade fica presa aqui até sair
    return x


def superDigit(n, k):
    n = n*k
    z = list(n)
    valores = [int(val) for val in z]
    j = sum(valores)
    if j < 10:
        return j
    return superDigit(str(j), 1)