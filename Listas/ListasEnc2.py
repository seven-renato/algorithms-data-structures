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