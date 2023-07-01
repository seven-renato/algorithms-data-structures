
import unicodedata

def piramide(x, y):
    cont = 0
    space = y
    letter = str(x)
    while cont < y:
        print(" "*space, letter)
        letter += 2*str(x)
        space -= 1
        cont = cont + 1

def escadinha(x,y):
    cont = 0 
    word = x
    while cont < y:
        print(word)
        word = word + x
        cont = cont + 1

def fatorial(x):
    cont = x
    xfat = 1
    while cont > 0:
        xfat = xfat * cont
        cont = cont - 1
    return(xfat)

def fibonnaci(x):
    cont = 0
    i = 1
    j = 0
    while cont < x:
        print(j)
        i = i + j 
        j = i - j 
        cont = cont + 1

def eh_primo(x):
    cont = 2
    if x == 1 or x == 2:
        return(True)
    if x % 2 == 0:
        return(False)
    while cont < x:
        if x % cont == 0:
            return(False)
        cont = cont + 1
    return(True)

def primosintervalo(x,y):
    cont = 0
    while cont < y+1:
        if eh_primo(x) == True:
            print(x)
        cont = cont + 1
        x = x + 1

def intervaloprimo(x,y):
    for i in range (x,y+1):
        if eh_primo(i) == True:
            print(i)

def justify(num):#999
  if num < 10:
    saida = "0"
  else: 
    saida = " "
  return(saida+num)

def soma(x,y):
  return(x+y)

def subtracao(x,y):
  return(x-y)

def multiplicacao(x,y):
  return(x*y)

def divisao(x,y):
  if y == 0:
    return(-1)
  else:
    return(x/y)

def exponenciacao(x,y):
  if type(y) != int:
    return(-1)
  else:
    return(x**y)

def pi ():
    k = 0#cont
    y = 0
    while k < 10000:
        x = ((-1)**k)/((2*k)+1)
        y = y + x
        k = k + 1
    pi = 4*(y)
    return(pi) 

def permutatacao(n,p):
  permutacao = fatorial(n)/(fatorial(n-p))
  return(permutacao)

def combinacao(n,p):
  combinacao = fatorial(n)/(fatorial(p)*(fatorial(n-p)))
  return combinacao

def somatorio (i,f):
  x = (i-1)
  somatorio = 0
  if type(i) != int or type(f) != int:
    return(-1)
  if i > f:
    return(0)
  if i == f:
    return(i)
  while x < f:
    somatorio = somatorio + (i)
    i = i + 1
    x = x + 1
  return(somatorio)

def exp(x):
  k = 0
  y = 0
  while k < 100:
    expx = (x**k)/fatorial(k)
    k = k + 1
    y = y + expx
  return(y)

def ln(x):
  k = 0
  y = 1
  z = ((x-1)/(x+1))
  v = 0
  t = 0
  while k < 101:
    logex = z * ((1/y)*(z**v))
    v = v + 2
    y = y + 2
    k = k + 1
    t = t + logex
  inx = 2*t
  return(inx)

def superExponenciacao(x,y):
  return(exp(y*(ln(x))))

def raizQuadrada(x):
  return(exp(1/2*(ln(x))))

def somalista(numeros):
    soma = 0
    for i in numeros:
        soma = soma + i
    return soma

def somatorioentre (i,f):
  x = i
  somatorio = 0
  if type(i) != int or type(f) != int:
    return(-1)
  if i > f:
    return(0)
  if i == f:
    return(i)
  while x < (f-1): #9 < 9
    somatorio = somatorio + (i+1) #44
    i = i + 1 #9
    x = x + 1 #9
  return(somatorio)

def somatorioentre2 (i,f):
  if type(i) != int or type(f) != int:
    try:
      i = int(i)
      f = int(f)
    except:
      return(-1)
  x = i
  somatorio = 0
  if i > f:
    return(0)
  if i == f:
    return(i)
  while x < (f-1): #9 < 9
    somatorio = somatorio + (i+1) #44
    i = i + 1 #9
    x = x + 1 #9
  return(somatorio)

def data(x,y,z):
  if ((x > 31 or x < 1) or (y > 12 or y < 1) or (z < 1)):
      return("A data NÃO existe!")
  elif (z % 4 == 0 and y == 2 and x > 29):
      return("A data NÃO existe!")
  elif (z % 4 != 0 and y == 2 and x > 28):
      return("A data NÃO existe!")
  elif ((y == 4 or y == 6 or y == 9 or y == 11) and x > 30):
      return("A data NÃO existe!")
  else:
      return("A data existe!")

def tabuada():
  cont = 0
  mult = 0
  while cont < 11:
    print("Tabuada do:", cont)
    while mult < 11:
      resultado = cont * mult
      print(cont, "x", mult, "==", resultado)
      mult = mult + 1
    cont = cont + 1
    mult = 0

def fiborecursiva(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    return fiborecursiva(x-1) + fiborecursiva(x-2)

def superDigit(n,k):
    n = n*k
    z = list(n)
    valores = [int(val) for val in z]
    j = sum(valores)
    if j < 10:
        return j
    return superDigit(str(j),1) 

def squareRoot2(n): 

    if n == 0: 
        return 2 
    x = 2+1/squareRoot2(n-1) # a recursividade fica presa aqui até sair
    return x

def maiornumero(x,y,z):
    maior_numero = max(x,y,z)
    return(maior_numero)
def menornumero(x,y,z):
    menor_numero = min(x,y,z)
    return(menor_numero)

def tira_acento(string: str) -> str:
    normalized = unicodedata.normalize('NFD', string)
    return normalized.encode('ascii', 'ignore').decode('utf8').casefold()