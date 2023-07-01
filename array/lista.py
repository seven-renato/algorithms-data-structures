def questao1():
    tam = int(input("Insira o tamanho da lista: "))
    k = 0
    k2 = 0
    lista = []
    while k < tam:
        num = float(input("Digite os números da lista: "))
        lista.append(num)
        k +=1

    qual = float(input("Digite o parâmetro: "))

    if qual in lista:
        while lista[k2] != qual:
            k2 += 1
        print("Indice do parâmetro ==",k2)
    else:
        print("False")

def questao2():
    i = 1
    lista = []
    while i != 0:
        i = abs(int(input()))
        lista.append(i)
    lista.pop() # retira o ultimo elemento

    lista_reversa = []
    cont = len(lista)-1

    while cont >= 0:
        lista_reversa.append(lista[cont])
        cont -= 1
    print(lista_reversa)

def questao3():
    tam = int(input("Insira o tamanho da lista: "))
    k = 0
    k1 = 0
    k2 = 0
    lista = []
    while k < tam:
        num = float(input("Digite os números da lista: "))
        lista.append(num)
        k += 1

    qual = float(input("Valor a ser verificado: "))

    if qual in lista:
        while k2 < len(lista):
            if lista[k2] == qual:
                k1 += 1
            k2 += 1
        print(f"Número de vezes que {qual} repete:", k1)
    else:
        print(0)