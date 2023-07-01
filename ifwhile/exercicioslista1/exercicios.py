def questao1b():
    cont = 0
    while cont < 10:
        print("este nome")
        cont = cont + 1
def questao1a(x,y):
    for i in range (y):
        print(x)

def questao2(a,b,c):
    maior = a
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    return maior

def questao3(a,b):
    return (a//b)

def questao4(a,b):
    if a <= 0 or b <= 0:
        return(-1)
    else:
        return (a*b)

def questao5():
    x = input("Digite a senha: ")
    while x != "PASSEI!":
        x = input("(ERROR) Digite a senha novamente: ")

def questao6(x):
    if x == 0:
        return(False)
    elif x % 3 == 0:
        return(True)
    else:
        return(False)

def questao7(a,b,c,d,e):
    return( (a+b+c+d+e)/5)

def questao8(x):
    return round(x*5.29,2)

def questao9():
    s = int(input("Insira o número de bermudas do tamanho pequeno: "))
    m = int(input("Insira o número de bermudas do tamanho medio: "))
    b = int(input("Insira o número de bermudas do tamanho grande: "))
    eb = int(input("Insira o número de bermudas do tamanho extra grande: "))

    ps = 8 * s
    pm = 10 * m
    pb = 14 * b
    peb = 18 * eb
    z = (ps + pb + peb + pm)
    print("Preço total foi de: R$",z)
  
def questao10(x):
    multa = x - 60
    if multa > 0:
        return(multa*3)

def questao11():
    x = input()
    z = input()
    if x == z:
        return("Empate")
    elif x == "pedra" and z == "papel":
        return("O jogador 2 ganhou")
    elif x == "papel" and z == "pedra":
        return(("O jogador 1 ganhou"))
    elif x == "pedra" and z == "tesoura":
        return ("O jogador 1 ganhou")
    elif x == "tesoura" and z == "pedra":
        return("O jogador 2 ganhou")
    elif z == "pedra" and x == "papel":
        return("O jogador 1 ganhou")
    elif z == "papel" and x == "pedra":
        return(("O jogador 2 ganhou"))
    elif z == "pedra" and x == "tesoura":
        return ("O jogador 2 ganhou")
    elif z == "tesoura" and x == "pedra":
        return("O jogador 1 ganhou")

def questao12():
    num1,num2,num3,num4 = map(int,input().split())
    if num1 < 1 or num1 > 255:
        return(False)
    elif num2 < 0 or num2 > 255:
        return (False)
    elif num3 < 0 or num3 > 255:
        return (False)
    elif num4 < 0 or num4 > 255:
        return (False)
    else:
        return("É valido e seu ip inserido é de: {}.{}.{}.{}".format(num1,num2,num3,num4))

def questao13():
    nome = input("Digite seu nome: ")
    cont = 0
    soma = 0
    while cont < 7:
        nota = float(input("Insira a nota do jurado: ")) 
        if cont == 0:
            maior_nota = nota
            menor_nota = nota
        if nota > maior_nota:
            maior_nota = nota
        if nota < menor_nota:
            menor_nota = nota
        soma += nota
        cont = cont + 1
    soma += (-1*(maior_nota + menor_nota))
    media = soma/5
    print(nome,"a sua nota média foi de: ", media)

def questao14(x):
    if x < 0:
        return(-1)
    if x % 2 == 0:
        soma = x+1
        cont = 0
        while cont < 6:
            print(soma)
            soma = soma + 2
            cont = cont + 1
    else:
        soma = x
        cont = 0
        while cont < 6:
            print(soma)
            soma = soma + 2
            cont = cont + 1

def questao15():
    x = 3
    for i in range (10,33):
        print(i*x) 

def questao16():
    cont = 0
    soma = 0
    while soma < 10:
        while cont < 60:
            print(f"{soma:02}:{cont:02}")
            cont = cont + 1
        cont = 0 
        soma += 1
    print(f"{soma:02}:{cont:02}")

def questao17(a,b,c):
    if a <= b and b <=c:
        return True
    else:
        return False

def questao18 (x,y):
    teste1 = x // y
    teste2 = x/y
    teste = y*(teste2 - teste1)
    return (f"{teste:2f}")

def questao19():
    num = int(input("Digite um número: "))
    cont = 0
    cont2 = 0
    numteste = num
    while num > 1000 or num < 10:
        num = int(input("Erro - Digite um número até mil e maior q 9: "))
    if num % 10 == 0:
        cont = 1
        if num % 100 == 0:
            while numteste > 100:
                numteste -= 100
                cont = cont + 1
            print(f"{cont:03}")
        elif num % 10 == 0 and num < 100:
            while numteste > 10:
                numteste -= 10
                cont = cont + 1
            print(f"{cont:02}")
        else:
            while numteste > 100:
                numteste -= 100
                cont = cont + 1
            if numteste > 10:
                cont = cont - 1
                cont2 = 1
                while numteste > 10:
                    numteste -= 10
                    cont2 = cont2 + 1
            print(f"0{cont2}{cont}")
    elif num > 100:
        while numteste > 100:
            numteste = numteste - 100
            if numteste < 100:
                numteste2 = numteste
                while numteste2 > 10:
                    numteste2 -= 10
                    cont2 = cont2 + 1
                    numfinal = numteste2
            cont = cont + 1
        print((numfinal*100) + (cont2*10) + cont)
    else:
        while numteste > 10:
            numteste -= 10
            cont = cont + 1
        numteste2 = numteste
        print((numteste2*10) + (cont))

def questao20(x,y):
    if x > y:
        maior = x
    else:
        maior = y
    while True:
        if maior % x == 0 and maior % y == 0:
            print(maior)
            break
        else:
            maior += 1                       