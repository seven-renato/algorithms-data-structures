def checkColuna(a,b,c):
    for i in range(3):
        if a[i] == b[i] and b[i] == c[i] and a[i] != ".":
            return a[i]
    return False

def checkLinha(a,b,c):
    vet = [a,b,c]
    for i in range(3):
        if vet[i][0] == vet[i][1] and vet[i][1] == vet[i][2] and vet[i][0] != ".":
            return vet[i][0]
    return False
        
def checkDiagonal(a,b,c):
    vet = [a,b,c]
    if vet[0][0] == vet[1][1] and vet[1][1] == vet[2][2] and vet[1][1] != ".":
        return vet[0][0]
    if vet[0][2] == vet[1][1] and vet[1][1] == vet[2][0] and vet[1][1] != ".":
        return vet[0][2]
    return False

def acabou(a,b,c):
    vet = [a,b,c]
    for i in range(3):
        for j in range(3):
            if vet[i][j] != ".":
                acabou = True
            else:
                return False
    return acabou

a = [".",".", "."]
b = [".",".", "."]
c = [".",".", "."]
posicoes_possiveis = ["a","b","c"]
print(f"   1     2     3")
print(f"A {a}\nB {b}\nC {c}")
posicoes_usadas = []
print("Digite a posição onde será colocada a peça. Por exemplo A1, seria o índice a11 da tabela.\n ")
while True:
    #X
    xposicao = input("Digite a posição onde o 'X' deve ser colocado: ").lower()
    while xposicao in posicoes_usadas or ('a' not in xposicao and 'b' not in xposicao and 'c' not in xposicao):
        xposicao = input("Digite a posição onde o 'X' deve ser colocado(note que deve ser em posições diferentes): ").lower()
    posicoes_usadas.append(xposicao)
    x = list(xposicao)
    x[1] = int(x[1]) - 1
    if x[0] == "a":
        a[x[1]] = "X"
        print(f"A {a}\nB {b}\nC {c}")
    elif x[0] == "b":
        b[x[1]] = "X"
        print(f"A {a}\nB {b}\nC {c}")
    elif x[0] == "c":
        c[x[1]] = "X"
        print(f"A {a}\nB {b}\nC {c}")
    
    #Testes de vitória
    if checkColuna(a,b,c) != False or checkDiagonal(a,b,c) != False or checkLinha(a,b,c) != False:
        print("Ganhou! O jogador 1, que estava com 'X' (xis).")
        break
    
    if acabou(a,b,c):
        print("Empate!")
        break
    #O
    oposicao = input("Digite a posição onde o 'O' deve ser colocado: ").lower()
    while oposicao in posicoes_usadas or ('a' not in oposicao and 'b' not in oposicao and 'c' not in oposicao):
        oposicao = input("Digite a posição onde o 'O' deve ser colocado(note que deve ser em posições diferentes): ").lower()
    posicoes_usadas.append(oposicao)
    o = list(oposicao)
    o[1] = int(o[1]) - 1
    if o[0] == "a":
        a[o[1]] = "O"
        print(f"A {a}\nB {b}\nC {c}")
    elif o[0] == "b":
        b[o[1]] = "O"
        print(f"A {a}\nB {b}\nC {c}")
    elif o[0] == "c":
        c[o[1]] = "O"
        print(f"A {a}\nB {b}\nC {c}")

    #Testes de vitória
    if checkColuna(a,b,c) != False or checkDiagonal(a,b,c) != False or checkLinha(a,b,c) != False:
        print("Ganhou! O jogador 2, que estava com 'O'(bolinha). ")
        break
    
    if acabou(a,b,c):
        print("Empate!")
        break