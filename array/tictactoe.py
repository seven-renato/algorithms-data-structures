a = [".",".", "."]
b = [".",".", "."]
c = [".",".", "."]
posicoes_possiveis = ["a","b","c"]
print(f"   1     2     3")
print(f"A {a}\nB {b}\nC {c}")
posicoes_usadas = []
print("Digite a posição onde será colocada a peça. Por exemplo A1, seria o índice a11 da tabela.\n ")
teste = True
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
    if a[0] == a[1] and a[1] == a[2] and a[0] == "X":
        print("Ganhou jogador 1(X)")
        teste = False
        break
    elif b[0] == b[1] and b[1] == b[2] and b[0] == "X":
        print("Ganhou jogador 1(X)")
        teste = False
        break
    elif c[0] == c[1] and c[1] == c[2] and c[0] == "X":
        print("Ganhou jogador 1(X)")#linha x
        teste = False
        break
    elif a[0] == b[0] and b[0] == c[0] and a[0] == "X":
        print("Ganhou jogador 1(X)")
        teste = False
        break
    elif a[1] == b[1] and b[1] == c[1] and a[1] == "X":
        print("Ganhou jogador 1(X)")
        teste = False
        break
    elif a[2] == b[2] and b[2] == c[2] and a[2] == "X":
        print("Ganhou jogador 1(X)")
        teste = False
        break
    elif a[0] == b[1] and b[1] == c[2] and a[0] == "X":
        print("Ganhou jogador 1(X)")
        teste = False
        break
    elif a[2] == b[1] and b[1] == c[0] and a[2] == "X":
        print("Ganhou jogador 1(X)")
        teste = False
        break
    elif a[0] == a[1] and a[1] == a[2] and a[0] == "O":
        print("Ganhou jogador 1(O)")
        teste = False
        break
    elif b[0] == b[1] and b[1] == b[2] and b[0] == "O":
        print("Ganhou jogador 1(O)")
        teste = False
        break
    elif c[0] == c[1] and c[1] == c[2] and c[0] == "O":
        print("Ganhou jogador 1(O)")#linha O
        teste = False
        break
    elif a[0] == b[0] and b[0] == c[0] and a[0] == "O":
        print("Ganhou jogador 1(O)")
        teste = False
        break
    elif a[1] == b[1] and b[1] == c[1] and a[1] == "O":
        print("Ganhou jogador 1(O)")
        teste = False
        break
    elif a[2] == b[2] and b[2] == c[2] and a[2] == "O":
        print("Ganhou jogador 1(O)")
        teste = False
        break
    elif a[0] == b[1] and b[1] == c[2] and a[0] == "O":
        print("Ganhou jogador 1(O)")
        teste = False
        break
    elif a[2] == b[1] and b[1] == c[0] and a[2] == "O":
        print("Ganhou jogador 1(O)")
        teste = False
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
    if a[0] == a[1] and a[1] == a[2] and a[0] == "X":
        print("Ganhou jogador 1(X)")
        teste = False
        break
    elif b[0] == b[1] and b[1] == b[2] and b[0] == "X":
        print("Ganhou jogador 1(X)")
        teste = False
        break
    elif c[0] == c[1] and c[1] == c[2] and c[0] == "X":
        print("Ganhou jogador 1(X)")#linha x
        teste = False
        break
    elif a[0] == b[0] and b[0] == c[0] and a[0] == "X":
        print("Ganhou jogador 1(X)")
        teste = False
        break
    elif a[1] == b[1] and b[1] == c[1] and a[1] == "X":
        print("Ganhou jogador 1(X)")
        teste = False
        break
    elif a[2] == b[2] and b[2] == c[2] and a[2] == "X":
        print("Ganhou jogador 1(X)")
        teste = False
        break
    elif a[0] == b[1] and b[1] == c[2] and a[0] == "X":
        print("Ganhou jogador 1(X)")
        teste = False
        break
    elif a[2] == b[1] and b[1] == c[0] and a[2] == "X":
        print("Ganhou jogador 1(X)")
        teste = False
        break
    elif a[0] == a[1] and a[1] == a[2] and a[0] == "O":
        print("Ganhou jogador 1(O)")
        teste = False
        break
    elif b[0] == b[1] and b[1] == b[2] and b[0] == "O":
        print("Ganhou jogador 1(O)")
        teste = False
        break
    elif c[0] == c[1] and c[1] == c[2] and c[0] == "O":
        print("Ganhou jogador 1(O)")#linha O
        teste = False
        break
    elif a[0] == b[0] and b[0] == c[0] and a[0] == "O":
        print("Ganhou jogador 1(O)")
        teste = False
        break
    elif a[1] == b[1] and b[1] == c[1] and a[1] == "O":
        print("Ganhou jogador 1(O)")
        teste = False
        break
    elif a[2] == b[2] and b[2] == c[2] and a[2] == "O":
        print("Ganhou jogador 1(O)")
        teste = False
        break
    elif a[0] == b[1] and b[1] == c[2] and a[0] == "O":
        print("Ganhou jogador 1(O)")
        teste = False
        break
    elif a[2] == b[1] and b[1] == c[0] and a[2] == "O":
        print("Ganhou jogador 1(O)")
        teste = False
        break
if teste:
    print("Deu empate na real. ")