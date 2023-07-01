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
    cont, cont2 = 0, 0
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

arq = open("C:\\Users\\seven\\Documents\\Projetos\\FURG\\AULA\\algortimo\\prova2\\exercicio-tabela\\tabela.csv","r")
lista = arq.readlines()
arq.close()
nova_lista = []
local = []
for linha in lista:
    nova_lista.append(linha[0:-1]) # IMPRIME DO NICIO ATÈ O PENULTIMO CARACTERE
for row in nova_lista:
    local.append(split(row,";"))

lista_nomes = [local[i][0] for i in range(len(local))]
while True:
    print("---> Digite '0' para acabar <---")
    nome = input("Digite o nome: ")
    if nome == '0':
        break
    while nome not in lista_nomes:
        nome = input("ERROR: Digite um nome da lista: ")
    for i in range (len(local)):
        if local[i][0] == nome:
            print("Ganha R$"+str(local[i][1]))
            resposta = input(f"Digite o novo salário do {local[i][0]}: ")
            local[i][1] = resposta
            print(f"Certo, alterado para {resposta}R$ o salário de {local[i][0]}.\n") 
            break

var = []
for i in range (len(local)):
    var.append(str(join(local[i],";")))
fim = join(var,"\n")
arq = open("C:\\Users\\seven\\Documents\\Projetos\\FURG\\AULA\\algortimo\\prova2\\exercicio-tabela\\tabela2.csv","w+")
arq.write(fim)
arq.close()