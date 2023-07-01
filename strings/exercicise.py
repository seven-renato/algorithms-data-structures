import random
from tkinter.filedialog import test
def uppercase(string):
    if ord(string) >=97 and ord(string) <=122:
      x = ord(string) - 32
      return chr(x)
    else: 
      return string
from itertools import product

def questao1():
    palavra = "Paulo#Renato Pereira das Neves Neto"
    palavra_fim = ""
    for letra in palavra:
        palavra_fim += uppercase(letra)
    return(palavra_fim)

def questao2():
    frase_ini = "O rato o roeu a roupa do rei de roma."
    frase = list(frase_ini)
    cont = 0
    while cont < len(frase):
        if frase[cont] == " ":
            frase[cont+1] = uppercase(frase[cont+1])
        cont += 1
    print(("").join(frase))

def questao2b():
    frase_ini = "O rato roeu a   roupa do rei de roma."
    frase = ""
    cont = 0
    proximo = False
    while cont < len(frase_ini):
        if proximo:
            frase += uppercase(frase_ini[cont])
            proximo = False
        else:
            frase += frase_ini[cont]
        if frase_ini[cont] == " ":
            proximo = True    
        cont += 1
    print(frase)

def questao2c():
    frase_ini = "O rato roeu a   roupa do rei de roma."
    frase = ""    
    proximo = False
    for letra in frase_ini:
        if proximo:
            frase += uppercase(letra)
            proximo = False
        else:
            frase += letra
        if letra == " ":
            proximo = True    

def questao3():
    senha = input("Digite a senha: ")
    maisculas = []
    num = []
    num_M = 65
    caracteres = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@']
    while num_M <= 90:
        maisculas.append(chr(num_M))
        num_M += 1
    for i in range(10):
        num.append(str(i))
    senha_Fraca = True
    senha_Media = True
    senha_Forte = True
    for letter in maisculas:
        if letter in senha:
            senha_Fraca = False
            senha_Media = False
    if senha_Media == True:
        for char in caracteres:
            if char in senha:
                senha_Media = True
                senha_Fraca = False
        for i in num:
            if i in senha:
                senha_Media = True
                senha_Fraca = False
    if senha_Fraca:
        print("Senha fraca.")
    elif senha_Media:
        print("Senha Média")
    elif senha_Forte:
        print("Senha Forte")

def questao4():
    chars  = [chr(i) for i in range(97, 123)]
    chars += [chr(i) for i in range(48, 58)]
    def criar_senha():
        senha = ""
        num_l = random.randint(1,6)
        for i in range(6-num_l):
            senha += str(random.randint(0,9))
        for i in range(num_l):
            senha += str(chr(random.randint(97,123)))
        senha_fim = list(senha)
        random.shuffle(senha_fim)
        return ("".join(senha_fim))
    def testar_senha(senha):
        senha_teste = criar_senha()
        senha_testadas = [senha_teste]
        cont = 0
        while senha_teste != senha:
            if senha_teste in senha_testadas:
                senha_teste = criar_senha()
            senha_testadas.append(senha_teste)
            cont += 1
        return cont     
    def testa_iter(chars,senha):
        tentativa = 0
        for i in product(chars, repeat=6):
            combina = ''.join(i)
            tentativa += 1
        
            if (tentativa % 500000 == 0):
                print('%10i --> %s' % (tentativa, combina))

            if  senha == combina:
                return('Senha encontrada é "{}", após {} tentativas.'.format(combina, tentativa))
        return ('Senha NÃO encontrada')
    return testa_iter(chars,criar_senha())

print(questao3())