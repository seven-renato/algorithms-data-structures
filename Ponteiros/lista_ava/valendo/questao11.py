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

if m != a or b != n:
    print("Não é possivel calcular a multiplicação!")
else:
    matriz_aux = []
    matriz2 = []
    for i in range(a):
        for j in range(b):
            matriz_aux.append(random.randint(4,8))
        matriz2.append(matriz_aux)
        matriz_aux = []   
 
    matriz_aux = []
    matriz = []
    for i in range(m):
        for j in range(n):
            matriz_aux.append(matriz1[i][j] + matriz2[i][j])
        matriz.append(matriz_aux)
        matriz_aux = []
    print(matriz1)
    print(matriz2)
    print(matriz)