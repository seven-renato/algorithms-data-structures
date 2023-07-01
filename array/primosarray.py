
def array_primo(x):
    if x == 1 or x == 0:
        return -1
    primos = [2,3]
    if x == 2:
        primos.pop()
    cont = 3
    while cont < (x+1):
        eh_primo = True
        for j in primos:
            if cont % j == 0:
                eh_primo = False
        if eh_primo:
            primos.append(cont)
        cont += 2
    return primos

print(array_primo(9))
