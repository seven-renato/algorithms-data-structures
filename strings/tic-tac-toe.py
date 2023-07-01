def checkLinhas(a):
  if a[0] != "." and a[0] == a[1] and a[1] == a[2]:
    print("Ganhou o jogador ({})".format(a[0]))
    return True
  return False
def checkColuna(a,b,c):
  i = 0
  while i < 3:
    if a[i] != "." and a[i] == b[i] and b[i] == c[i]:
      print("Ganhou o jogador ({})".format(a[i]))
      return True
    i += 1
  return False
def checkDiag(a,b,c):
  vet = [[0,1,2],[2,1,0]]
  i = 0
  while i < len(vet):
    minivet = vet[i]
    if a[minivet[0]] != "." and a[minivet[0]] == b[minivet[1]] and b[minivet[1]] == c[minivet[2]]:
      print("Ganhou o jogador ({})".format(b[1]))
      return True
    i += 1
  return False

a = [".",".", "."]
b = [".",".", "."]
c = [".",".", "."]
matriz = [a, b, c]
posicoes_possiveis = ["a","b","c"]
print(f"   1     2     3")
print(f"A {a}\nB {b}\nC {c}")
posicoes_usadas = []
print("Digite a posição onde será colocada a peça. Por exemplo A1, seria o índice a11 da tabela.\n ")
teste = True
cont = 0
while True:
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
    for linha in matriz:
      if checkLinhas(linha):
        teste = False
        break
    if checkColuna(a,b,c):
        teste = False
    if checkDiag(a,b,c):
        teste = False
    if teste == False:
        break
    if cont == 8:
        teste = True
        break
    cont += 1
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
    for linha in matriz:
      if checkLinhas(linha):
        teste = False
        break
    if checkColuna(a,b,c):
        teste = False
    if checkDiag(a,b,c):
        teste = False
    if teste == False:
        break
    if cont == 8:
        teste = True
        break
    cont += 1
if teste:
    print("Deu Velha!")

"""
b2
a3
b3
b1
c1
a2
a1
c3
c2
"""