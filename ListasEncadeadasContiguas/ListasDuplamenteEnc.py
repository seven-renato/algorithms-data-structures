class Nodo:
    def __init__(self, info):
        self.info = info
        self.prox = None
        self.ant = None

class ListaEnc:
    def __init__(self):
        self.inicio = None
        self.fim = None

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
    #Mudar
    def inserir(self, pos, valor):
        if(pos > 0 and pos <= self.getTamanho()+1):
            n = Nodo(valor)
            if self.inicio == None:
                self.inicio = n
                self.fim = n
            elif(pos == 1):
                self.inicio.ant = n
                n.prox = self.inicio
                self.inicio = n
            elif(pos == self.getTamanho()+1):
                self.fim = n
                aux = self.inicio
                cont = 1
                while aux.prox != None:
                    aux = aux.prox
                    cont += 1
                aux.prox = self.fim
                self.fim.ant = aux
            else:
                aux = self.inicio
                cont = 1
                while (cont < pos-1):
                    aux = aux.prox
                    cont += 1
                n.prox = aux.prox
                n.ant = aux
                aux.prox = n
            return True
        return False
    #Mudar
    def remover(self, pos):
        if pos > 0 and pos <= self.getTamanho():
            if pos == 1:
                self.inicio = self.inicio.prox
                if self.inicio != None:
                    self.inicio.ant = None
                else:
                    self.fim = None
            elif pos == self.getTamanho():
                self.fim = self.fim.ant
                self.fim.prox = None
            else:
                cont = 1
                ptAux = self.inicio
                while True:
                    if cont == pos-1:
                        ptAux.prox = ptAux.prox.prox
                        ptAux.prox.ant = ptAux
                        break
                    ptAux = ptAux.prox
                    cont += 1
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
    # Mudar
    def destroi(self):
        while self.inicio != None:
            self.remover(1)
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

    def imprimeAoContrario(self):
        l = ListaEnc()
        aux = self.inicio
        while (aux != None):
            l.inserir(1, aux.info)
            aux = aux.prox
        l.imprimir()
        l.destroi()


    def imprimirParesAoContrario(self):
        vet = [self.valor(pos) for pos in range(1,self.getTamanho()+1)][::-2]
        for val in vet:
            print(val)

    def imprimirParesAoContrario2(self):
        cont = 1 
        ptaux = self.fim
        while ptaux != None:
            if cont % 2 != 0:
                print(ptaux.info)
            ptaux = ptaux.ant
            cont += 1


    def limpar(self):
        self.inicio = self.inicio.prox
        while self.inicio != None:
            self.inicio.ant = None
            self.inicio = self.inicio.prox
        self.fim = None

l = ListaEnc()

l.inserir(1,"oi")
l.inserir(1,"oi13")
l.inserir(1,"oi12")
l.inserir(1,"oi10")
l.inserir(1,"oi9")
l.inserir(1,"oi8")
l.inserir(1,"oi7")
l.inserir(1,"oi6")
l.inserir(1,"oi5")
l.inserir(1,"oi4")
l.inserir(1,"oi3")
l.inserir(1,"oi2")
l.inserir(1,"oi1")

l.imprimir()
print("--->")
l.imprimirParesAoContrario()
print("--->")
l.imprimirParesAoContrario2()

# l.limpar()
# print("OI")
# l.imprimir()
# l.limpar()