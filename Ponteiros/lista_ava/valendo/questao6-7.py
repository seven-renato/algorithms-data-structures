lista1 = [1,4,5,7,10]
lista2 = [0,2,5,7,11]

lista3 = []
for val in lista1:
    lista3.append(val)
for val in lista2:
    lista3.append(val)
print(lista3, sum(lista3))

lista3 = list(set(lista3))
print(lista3)