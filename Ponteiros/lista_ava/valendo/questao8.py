import random

lista1 =[]
lista2 =[]
lista3 =[]
for i in range(5):
    lista1.append(random.randint(-10,10))
    lista2.append(random.randint(-10,10))
    lista3.append(random.randint(-10,10))
matriz = [lista1,lista2,lista3]
print(matriz)
maior = -10
maioresvalores = []
for val in matriz:
    maioresvalores.append(max(val))
print(max(maioresvalores))    
#teste = max([max(lista3),max(lista2),max(lista1)])
#print(teste)