import random
import itertools as it

def criar_senha():
    numero_num = random.randint(0,6)
    numero_letra = 6 - numero_num
    senha_gerada = ""
    for i in range (numero_num):
        numero = random.randint(0,9)
        senha_gerada += str(numero)
    for i in range (numero_letra):
        letra = random.randint(65,90)
        senha_gerada += chr(letra)
    print(senha_gerada)

def achar_senha(senha):
    char = [chr(val) for val in range(48,58)]
    char += [chr(val) for val in range(ord("A"),ord("Z")+1)]
    combina = ""
    tentativa = 0
    for a in char:
        for b in char:
            for c in char:
                for d in char:
                    for e in char:
                        for f in char:
                            combina = a+b+c+d+e+f
                            tentativa += 1
                            if tentativa % 5000000 == 0:
                                print(combina)
                            if senha == combina:
                                print("Achou sua senha é: ", combina)
                                return()

            
senha = criar_senha()
print(senha)
achar_senha("AAAAAA")

