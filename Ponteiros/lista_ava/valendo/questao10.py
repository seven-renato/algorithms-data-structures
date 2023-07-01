def contaEspaco(string):
    num = 0
    lista = []
    for letra in string:
        if letra == " ":
            num += 1
        else:
            lista.append(num)
            num = 0
    return max(lista)

print(contaEspaco("OI     eu sou o paulo   renato pereira    das neves  netoola"))
