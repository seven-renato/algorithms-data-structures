frase = "Paulo Renato Pereira das Neves Neto"
lista = frase.split(" ")
print(lista)
lista2 = frase.split("a")
print(lista2)
"""import random
random.seed()
lista = [0,0,0,0,0]
for i in range(10000):
    num = random.randint(0,4)
    lista[num] += 1
print(lista)"""
#csv - comma separated value

produto = "Carro;50"
print("-----------")
print(produto)
lista3 = produto.split(";")
print(lista3)