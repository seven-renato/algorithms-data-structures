arquivo = open("C:\\Users\\seven\\Documents\\Projetos\\FURG\\AULA\\algortimo\\strings\\questao6.txt","r")
read = arquivo.readlines() # read.write("") não necessariamente ele salva no hd, mas anota pelo momento, é melhor anotar tudo e dps qnd acaba de dar input #o close permite não dar erro
arquivo.close() # é importante fechar pois o arquivo pode ficar sequestrado pelo programa
def uppercase(string):
    if ord(string) >= 97 and ord(string) <= 122:
        x = ord(string) - 32
        return chr(x)
    else:
        return string
def upper(frase):
    palavra_fim = ""
    for letra in frase:
        palavra_fim += uppercase(letra)
    return (palavra_fim)

def cifra(frase,n):
    frase_fim = ""
    for letter in (upper(frase)):
        if letter == " ":
            frase_fim += letter
        else:
            num = ord(letter) + (n) 
            if num > ord("Z"):
                num -= 26
            letra = chr(num)
            frase_fim += letra
    return frase_fim

def descriptografar(frase,n):
    frase_fim = ""
    for letter in (upper(frase)):
        if letter == " ":
            frase_fim += letter
        else:
            num = ord(letter) - (n) 
            if num < ord("A"):
                num += 26
            letra = chr(num)
            frase_fim += letra
    return frase_fim

for i in range (len(read)):
    n = int(input("Digite o número de casas que devem ser criptografadas: "))
    palavra = cifra(read[i],n)
    print(palavra)
    print(descriptografar(palavra,n))
