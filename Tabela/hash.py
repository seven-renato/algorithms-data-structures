def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def proximo_primo(n):
    if n < 2:
        return 2
    achei_primo = False
    while not achei_primo:
        n += 1
        if eh_primo(n):
            achei_primo = True
    return n
class Nodo:
    def __init__(self, info):
        self.info = info
        self.prox = None
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

    def inserir(self, pos, valor):
        if(pos > 0 and pos <= self.getTamanho()+1):
            n = Nodo(valor)
            if(pos == 1):
                n.prox = self.inicio
                self.inicio = n
            else:
                aux = self.inicio
                cont = 1
                while (cont < pos-1):
                    if(aux.prox != None):
                        aux = aux.prox
                    cont += 1
                print(n)
                n.prox = aux.prox
                aux.prox = n
            return True
        return False

    def remove(self, pos):
        if pos > 0:
            if pos == 1:
                self.inicio = self.inicio.prox
                return True
            elif pos <= self.getTamanho():
                cont = 0
                ptAux = self.inicio
                while True:
                    if cont == pos-2:
                        aux = ptAux.prox.prox
                        ptAux.prox = aux
                        break
                    ptAux = ptAux.prox
                    cont += 1
                return True
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
                return 0
            
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
    
    def buscaRecursiva(self, valor, aux = -1,):
        if aux == -1:
            aux = self.inicio
        if aux == None:
            return (-self.getTamanho())
        if valor == aux.info:
            return 1
        return 1 + self.buscaRecursiva(valor, aux.prox)      
class TabelaHash:
    def __init__(self, tamanho):
        self.tamanhoMedio = tamanho
        self.hash = proximo_primo(tamanho)
        self.vet = [None]*self.hash

    def insere(self, vet):
        pos = vet[0]
        if self.vet[pos%self.hash] == None:
            lista = ListaEnc()
            lista.inserir(1,vet)
            self.vet[pos%self.hash] = lista
            return True
        self.vet[pos%self.hash].inserir(1, vet)
        return True
    
    def buscar(self, chave):
        if self.vet[chave%self.hash] != None:
            ptaux = self.vet[chave%self.hash].inicio
            while ptaux != None:
                print(ptaux.info[0])
                if ptaux.info[0] == chave:
                    return ptaux.info[1]
                ptaux = ptaux.prox
        return False
    
    def remover(self, chave):
        if self.vet[chave%self.hash] != None:
            ptaux = self.vet[chave%self.hash].inicio
            cont = 1
            while ptaux != None:
                if ptaux.info[0] == chave:
                    return self.vet[chave%self.hash].remove(cont)
                ptaux = ptaux.prox
                cont += 1
        return True

table = TabelaHash(7)
print(table.vet)
table.insere([73, "João"])
print(table.vet)
table.insere([84, "AA"])
table.insere([95, "AAB"])
print(table.buscar(73))
print(table.buscar(12))
print(table.remover(73))
print(table.buscar(73))
print(table.buscar(84))