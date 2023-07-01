# Questão 1
def somaIter(vet):
    soma = 0
    for val in vet:
        soma += val
    return soma

def somaRec(vet):
    if len(vet) == 1:
        return vet[0]
    return vet[0] + somaRec(vet[1:])

print("Questão 1:")
vet = [1, 2, 3, 10]
print(somaIter(vet))
print(somaRec(vet))

# Questão 2
def fatorialIter(valor):
    if valor == 0:
        return 1
    aux = 1
    while valor > 1:
        aux *= valor
        valor -= 1
    return aux

def fatorialRec(valor):
    if valor == 0 or valor == 1:
        return 1
    return valor * fatorialRec(valor-1)
print("Questão 2:")
print(fatorialIter(5)) 
print(fatorialRec(5))

def fiboRec(n):
    if n == 1 or n == 0:
        return 1
    if n == 2:
        return 1
    return fiboRec(n-2) + fiboRec(n-1)

def fiboIter(n):
    if (n==1) or (n==2):
        return 1
    count=3
    ultimo=1
    penultimo=1
    while count <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    return (termo)
print("Questão 3:")
print(fiboIter(20))
print(fiboRec(20))

def soma_digitos(valor):
    if valor == 0:
        return 0
    return valor%10 + soma_digitos(valor//10)

print(soma_digitos(9))