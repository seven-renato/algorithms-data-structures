def getLinha(matriz, n):
    return matriz[n]

def getColuna(matriz, n):
    return [val[n] for val in matriz]

def multiplicarLinhaColuna(linha,coluna):
    lista = []
    for i in range(len(linha)):
        lista.append(linha[i]*coluna[i])
    return sum(lista)

import random
print("Matriz 1")
m = int(input("Digite o numero do linhas: "))
n = int(input("Digite o numero do colunas: "))
matriz_aux = []
matriz1 = []
for i in range(m):
    for j in range(n):
        matriz_aux.append(random.randint(0,4))
    matriz1.append(matriz_aux)
    matriz_aux = []
print("Matriz 2")
a = int(input("Digite o numero do linhas: "))
b = int(input("Digite o numero do colunas: "))

if n != a:
    print("Não é possivel calcular a multiplicação!")
else:
    matriz_aux = []
    matriz2 = []
    for i in range(a):
        for j in range(b):
            matriz_aux.append(random.randint(4,8))
        matriz2.append(matriz_aux)
        matriz_aux = []    
    
    matriz1linha = len(matriz1)
    #matriz1col = len(matriz1[0])

    #matriz2lin = len(matriz2)
    matriz2coluna = len(matriz2[0])

    matrizResultante = []
    for i in range(matriz1linha):
        matrizResultante.append([])
        for j in range(matriz2coluna):
            matrizResultante[i].append(multiplicarLinhaColuna(getLinha(matriz1,i),getColuna(matriz2,j)))
    print(matrizResultante)