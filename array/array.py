compras = ["banana", "laranja", "maçã", "carne"]
print(compras)
print("O índice começa em zero: ", compras[0])
print("O próximo elemento: ", compras[1])
print("Ultimo elemento: ", compras[-1], compras[len(compras)-1])
print("Penúltimo elemento: ", compras[-2])
print("Tamanho da lista: ", len(compras))


compras.append("iogurt") # Append adiciona no fim do array
compras.append("kiwi")
compras.append(3.14) # Tipos dinâmicos

print("Tamanho da lista: ", len(compras))
uma_lista = []

higiene = ["sabonete", "shampoo", "papel higiênico", "pasta de dente"]
compras.append(higiene)
print(compras)
# ["banana", "laranja", "maçã", "carne","sabonete", ["shampoo", "papel higiênico", "pasta de dente"]]
# Uma lista dentro da lista, conta apenas um elemento

print("-->",type(compras[7]))
print("-->", type(compras[7][0]), compras[7][0]) # list, sabonete

for i in range (len(compras)):
  print("compras[{}] = {}".format(i,compras[i]))

print("-"*10)
cont = 0
cont2 = 0
while cont < len(compras):
    print("compras[{}] = {}".format(cont,compras[cont]))
    if cont == 7:
        print("-"*8)
        while cont2 < len(compras[7]):
            print("higiene[{}] = {}".format(cont2,compras[-1][cont2]))
            cont2 += 1
    cont = cont + 1