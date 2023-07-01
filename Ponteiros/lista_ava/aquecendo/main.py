import random
def questao1e2():
    n = int(input())
    lista = []
    cont = 0
    numeroDeZero = 0
    while cont < n:
        escolha = random.randint(-10,10)
        if escolha == 0:
            numeroDeZero += 1
        lista.append(escolha)
        cont += 1
    print(lista)
    # Medodo de  impor um fitlro sobre valores de uma lista usando função filter
    lista2 = list(filter(lambda x: x > 0, lista))
    lista3 = list(filter(lambda x: x < 0, lista))
    print(lista2, len(lista2))
    print(lista3, len(lista3))
    print(numeroDeZero, "numero de zeros")

def questao3():
    matriz = []
    matriz_aux = []
    for i in range (5):
        for j in range (10):
            matriz_aux.append(random.randint(0,10))
        matriz.append(matriz_aux)
        matriz_aux = []
    print(matriz)

    for i in range(10):
        print(f"Coluna {i+1}:")
        for j in range(5):
            print(matriz[j][i])
    
def questao4():
    n = int(input())
    lista = []
    for i in range(1,n+1):
        if n % i == 0:
            lista.append(i)
    print(lista)
    
#questao5
def potencia(x,y):
    if y == 1:
        return 1
    return potencia(x,y-1) * x

print(potencia(4,4))