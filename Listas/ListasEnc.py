class ListaEnc:
    def __init__(self):
        self.inicio = None

    def imprimir(self):
        ptAux = self.inicio
        while ptAux != None:
            print(ptAux.info)
            ptAux = ptAux.prox

    def getTamanho(self):
        cont = 0
        if self.inicio == None:
            return cont
        else:
            ptAux = self.inicio
            while ptAux != None:
                ptAux = ptAux.prox
                cont += 1
            return cont

    def inserir(self, node, pos):
        if self.inicio == None:
            self.inicio = node
        else:
            if pos > 0:
                if pos == 1:
                    ptaux = self.inicio
                    self.inicio = node
                    self.inicio.prox = ptaux
                elif pos < self.getTamanho() + 1:
                    cont = 0
                    ptAux = self.inicio
                    while True:
                        if cont == pos-2:
                            aux = ptAux.prox
                            ptAux.prox = node
                            ptAux.prox.prox = aux
                            break
                        ptAux = ptAux.prox
                        cont += 1
                else:
                    return False
            else:
                    return False

    def remove(self, pos):
        if pos > 0:
            if pos == 1:
                self.inicio = self.inicio.prox
            elif pos <= self.getTamanho() :
                cont = 0
                ptAux = self.inicio
                while True:
                    if cont == pos-2:
                        aux = ptAux.prox.prox
                        ptAux.prox = aux
                        break
                    ptAux = ptAux.prox
                    cont += 1
            else:
                return False
        else:
                return False
        
    def posicao(self, valor):
        cont = 1
        ptAux = self.inicio
        while True:
            try:
                if ptAux.info == valor:
                    return cont
                ptAux = ptAux.prox
                cont += 1
            except:
                return False
            
    def valor(self, pos):
        if pos > 0 and pos < self.getTamanho() + 1:
            cont = 1 
            ptAux = self.inicio
            while True:
                if cont == pos:
                    return ptAux.info
                ptAux = ptAux.prox
                cont += 1
        return False
    
    def destroi(self):
        self.inicio = None
        return True
    
    def listaAoContrario(self):
        vet = [self.valor(val) for val in range(1, self.getTamanho()+1)][::-1]
        for val in vet:
            print(val)
        return True

    def compara(self, lista2):
        ptAux = self.inicio
        ptAux2 = lista2.inicio
        while ptAux != None:
            if ptAux2.info != ptAux.info:
                return False
            ptAux = ptAux.prox
            ptAux2 = ptAux2.prox
        return True

class Nodo:
    def __init__(self, info, prox):
        self.info = info
        self.prox = prox

lista = ListaEnc()

pt1 = Nodo("5", None)
pt2 = Nodo("3", None)
pt3 = Nodo("12", None)
pt4 = Nodo("5123", None)


pt5 = Nodo("1323", None)
pt6 = Nodo("15", None)
pt7 = Nodo("231", None)
pt8 = Nodo("5333", None)

lista.inserir(pt1, 2)

pt1.prox = pt2
pt2.prox = pt3
pt3.prox = pt4



ptTeste = Nodo(13,None)
ptTeste4 = Nodo(58,None)
lista.inserir(pt5,1)
lista.inserir(pt6,1)
lista.inserir(pt7,1)
lista.inserir(pt8,1)
ptTeste10 = Nodo("AWKOPDKOPAWKOP",None)

lista.inserir(ptTeste, 1)
lista.inserir(ptTeste4, 2)

lista.inserir(ptTeste10, 15)
# lista.imprimir() 
print("DKWAKOPD")

print("-->", lista.getTamanho())
lista.remove(lista.getTamanho())
lista.remove(2)
lista.remove(1)

lista.imprimir() 
# print("-->",lista.valor(4))
print("-->")

#lista.destroi()
# lista.imprimir()
# print(lista.getTamanho())
lista.listaAoContrario()
print("-->")

lista2 = ListaEnc()
lista3 = ListaEnc()
lista2.inicio = pt1
lista2.imprimir()
lista3.inicio = pt1
print(lista.compara(lista2))
print(lista3.compara(lista2))
print(lista2.compara(lista3))