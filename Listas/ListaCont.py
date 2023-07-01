
class Lista:
    def __init__(self, max):
        self.max = max
        self.vetor = [None]*max
        self.ini = -1
        self.fim = -1

    def __repr__(self):
        string = "[ini"
        for i in range(self.ini, self.fim +1):
            string = string + "-->" + str(self.vetor[i]) + ", "
        return string + "]"
    
    def Limpar(self):
        self.vetor = self.max * [None]
        self.ini = -1
        self.fim = -1
        return True

    def Localizar(self, item):
        cont = 0
        for val in self.vetor:
            if val == item:
                return cont - self.ini + 1
            cont += 1
        return False
    
    def Acessar(self, k):
        if k < 0 or k > self.Tamanho() or self.Vazia():
            return False
        return self.vetor[self.ini+k-1]

    def Vazia(self):
        if (self.ini == -1) or (self.fim == -1):
            return True
        else:
            for val in self.vetor:
                if val != None:
                    return False
        return False
    
    def Tamanho(self):
        if not self.Vazia():
            return self.fim - self.ini + 1
        else:
            return 0
        

    def Insere(self, posicao, dado):
        if (self.ini == 0 and self.fim == self.max) or (posicao <= 0) or (posicao > self.Tamanho() + 1 and self.Vazia() == False): 
            return False
        else:
            if self.Vazia():
                self.ini = posicao-1
                self.fim = posicao-1
                self.vetor[self.ini] = dado
                return True
            elif (self.fim != self.max):
                print("entrei2")
                for i in range(self.fim, self.ini+posicao-2, -1):
                    try:
                        self.vetor[i+1] = self.vetor[i]
                    except:
                        pass
                self.fim += 1
            else:
                print("entrei")
                for i in range(self.ini, self.ini + posicao):
                    self.vetor[i-1] = self.vetor[i]
                self.ini -= 1
            self.vetor[self.ini + posicao - 1] = dado
            return True
        
    def remove(self, k):
        if self.Vazia():
            self.ini = -1
            self.fim = -1
            return False
        elif k <= 0 or k > self.Tamanho():
            return False
        if k == 1:
            self.vetor[self.ini] = None
            self.ini += 1
        elif k == self.fim - self.ini + 1:
            self.vetor[self.fim] = None
            self.fim -= 1
        elif self.fim == self.max and self.ini == 0:
            self.vetor[self.ini+k-1] = None
            for i in range(self.ini+k-1, self.ini, -1):
                    self.vetor[i] = self.vetor[i-1]
            self.vetor[self.ini] = None
            self.ini += 1
        else:
            self.vetor[self.ini+k-1] = None
            if k <= (self.fim - self.ini + 1)//2:
                print("3i")
                for i in range(self.ini+k-1, self.ini-1, -1):
                    self.vetor[i] = self.vetor[i-1]
                self.ini += 1
            else:
                for i in range(self.ini+k-1, self.fim-1):
                    self.vetor[i] = self.vetor[i+1]
                self.fim -= 1
                self.vetor[self.fim] = None
        



lista = Lista(15)


lista.Insere(15, "oi")
print(lista.vetor)
lista.Insere(1,"pinto")
# lista.Insere(1,"Carro1")
# print(lista.vetor)
# print(lista.ini)
# lista.Insere(2,"Carro3")
# print(lista.vetor)
# lista.Insere(2,"Carro2")
# print(lista.vetor)
# lista.Insere(1,"Carro13")
# print(lista.vetor)
# lista.remove(3)
# print(lista.vetor)
# lista.Insere(1,"Carro123")
# print(lista.vetor)
# lista.Insere(2,"Carro144")
# print(lista.vetor)
# lista.Insere(2,"Carrodaawdwd33")
# print(lista.vetor)
# lista.Insere(2,"Carro5136433")
# print(lista.vetor)
# lista.Insere(2,"Carro321 433")
# print(lista.vetor)
# lista.Insere(2,"Carro1233")
# print(lista.vetor)
# lista.Insere(2,"Carro1563")
# print(lista.vetor)
# lista.Insere(2,"Carraddaw")
# print(lista.vetor)
# lista.Insere(2,"Carro312333")
# print(lista.vetor)
# lista.Insere(2,"Pinto1422333123")
# print(lista.vetor)
# lista.Insere(2,"Pinto1422")
# print(lista.vetor)
# lista.Insere(2,"Pinto11")
# print(lista.vetor)
# lista.remove(1)
# print(lista.vetor)
# lista.remove(3)
# print(lista.vetor)
# print(lista.Acessar(10))
# lista.remove(10)
# print(lista.vetor)
# print(lista.Acessar(10))
# lista.remove(10)
# print(lista.vetor)
# print(lista.Acessar(10))
# lista.remove(4)
# print(lista.vetor)
# print(lista.Acessar(1))
# print(lista.ini)
# print("-->",lista.Acessar(9))
# print(lista.Localizar("Carro1"))

# lista.remove(3)
# print(lista.vetor)
# lista.Insere(2, "dadawkop")
# print(lista.vetor)
# lista.Insere(2, "dada32wkop")
# print(lista.vetor)
# lista.Insere(2, "dada52151523212132wkop")
# print(lista.vetor)
# lista.Insere(2, "32312")
# print(lista.vetor)
# lista.Insere(2, "32312")
# print(lista.vetor)
# lista.Insere(2, "32312")
# print(lista.vetor)
# lista.Insere(2, "12312332312")
# print(lista.vetor)
# lista.remove(3)

# print(lista.vetor)
# lista.remove(2)

# print(lista.vetor)
# lista.Insere(2, "32312")
# print(lista.vetor)
# lista.Insere(2, "12312332312")
# print(lista.vetor)
# lista.remove(2)

# print(lista.vetor)
# lista.remove(8)

# print(lista.vetor)
# lista.remove(1)
# lista.remove(1)
# lista.remove(1)
# lista.remove(1)
# lista.remove(12)
# lista.remove(1)
# lista.remove(1)
# lista.remove(1)

# print(lista.vetor)
# print(lista.ini)
# lista.remove(1)
# lista.remove(1)
# lista.remove(1)
# print(lista.vetor)
# lista.remove(3)
# print(lista.vetor)
# lista.remove(1)
# lista.remove(1)
# print(lista.vetor)
# print(lista.ini)
