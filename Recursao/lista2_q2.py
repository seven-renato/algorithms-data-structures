class Table:
    def __init__(self, tamanhoMax):
        self.chave = [None]*(tamanhoMax + 1)
        self.valor = [None]*(tamanhoMax + 1)
        self.li = 1
        self.ls = tamanhoMax
        self.ini = self.li - 1
        self.fim = self.ls + 1


    def vazia(self):
        return self.ini < self.li or self.fim > self.ls
    
    def cheia(self):
        return self.ini == self.li and self.fim == self.ls
    
    def tamanho(self):
        if not self.vazia():
            return self.fim - self.ini + 1
        return 0
        
    # def buscar(self, chave, opcao):
    #     if opcao == "binaria":
    #         return self.buscarBinaria(chave)
    #     else:
    #         return self.buscarLinear(chave)

    def buscar(self, chave):
        return self.buscaLinear(chave)

    def buscaLinear(self, chave):
        if not self.vazia():
            posicao = 0
            teste = False
            for val in self.chave:
                if val == chave:
                    teste = True
                    break
                posicao += 1
            if teste:
                return posicao
            else:
                return 0
        return 0

    def buscaLinearRec(self, chave, aux = None):
        if not self.vazia():
            if aux == None:
                aux = self.chave[1:self.fim+1]
            if len(aux) == 0:
                return -self.tamanho()
            if aux[0] == chave:
                return 1
            return 1 + self.buscaLinearRec(chave, aux[1:])
        return 0

    def buscaBinaria(self, chave):
        if self.vazia() or chave not in self.chave:
            return 0
        vet = self.chave[1:self.fim+1] # Faço um vetor simples, onde começa do inicio e vai até o fim tirando a primeira posição
        inicio = 0
        fim = len(vet) - 1
        while inicio <= fim:
            meio = (inicio + fim) // 2
            if vet[meio] == chave:
                return meio + 1
            elif vet[meio] < chave:
                inicio = meio + 1
            else:
                fim = meio - 1


    def inserirOrd(self, chave:int, valor):
        if self.vazia():
            self.ini = self.li
            self.fim = self.ini
            self.valor[self.ini] = valor
            self.chave[self.ini] = chave
        elif not self.cheia():
            posicao = self.buscaBinaria(chave)
            if posicao > 0:
                aux = []
                if type(self.valor[posicao]) == type(aux):
                    for val in self.valor[posicao]:
                        aux.append(val)
                else:
                    aux.append(self.valor[posicao])
                aux.append(valor)
                self.valor[posicao] = aux
                self.chave[posicao] = chave
            else:
                cont = 1
                teste = False
                for val in self.chave[self.ini: self.fim+1]:
                    if chave < val:
                        teste = True
                        break
                    cont += 1
                if teste:
                    for i in range(self.fim+1, self.ini+cont-1, -1):
                        self.valor[i] = self.valor[i-1]
                        self.chave[i] = self.chave[i-1]
                    self.valor[self.ini + cont -1] = valor
                    self.chave[self.ini + cont -1] = chave
                    self.fim += 1
                else:
                    self.valor[self.fim+1] = valor
                    self.chave[self.fim+1] = chave
                    self.fim += 1
        else:
            #print("Deu erro!")
            return False
        return True
    
    def inserirLinear(self, chave:int, valor):
        if self.vazia():
            self.ini = self.li
            self.fim = self.ini
            self.valor[self.ini] = valor
            self.chave[self.ini] = chave
        elif not self.cheia():
            posicao = self.buscar(chave)
            if posicao > 0:
                aux = []
                if type(self.valor[posicao]) == type(aux):
                    for val in self.valor[posicao]:
                        aux.append(val)
                else:
                    aux.append(self.valor[posicao])
                aux.append(valor)
                self.valor[posicao] = aux
                self.chave[posicao] = chave
            else:
                cont = 1
                teste = False
                for val in self.chave[self.ini: self.fim+1]:
                    if chave < val:
                        teste = True
                        break
                    cont += 1
                if teste:
                    for i in range(self.fim+1, self.ini+cont-1, -1):
                        self.valor[i] = self.valor[i-1]
                        self.chave[i] = self.chave[i-1]
                    self.valor[self.ini + cont -1] = valor
                    self.chave[self.ini + cont -1] = chave
                    self.fim += 1
                else:
                    self.valor[self.fim+1] = valor
                    self.chave[self.fim+1] = chave
                    self.fim += 1
                
        else:
            #print("Deu erro!")
            return False
        return True
    

    def remover(self,chave):
        posicao = self.buscar(chave)
        if posicao > 0:
            if posicao == self.fim:
                self.chave[self.fim] = None
                self.valor[self.fim] = None
            else:
                self.chave[posicao] = None
                self.valor[posicao] = None
                for i in range(posicao, self.ls):
                    val_chave = self.chave[i+1]
                    val_valor = self.valor[i+1]
                    self.chave[i] = val_chave
                    self.valor[i] = val_valor
                self.chave[self.fim] = None
                self.valor[self.fim] = None
            self.fim -= 1


    def consultar(self, chave):
        posicao = self.buscar(chave)
        if posicao > 0:
            return self.valor[posicao]

            
    def destruir(self):
        self.ini = self.li - 1
        self.fim = self.ls + 1

    def buscarBinariaRecursiva(self, chave):
        return self.__buscaBinRec(chave, 0, self.tamanho()-1, self.chave[1:self.fim+1]) + 1
    
    def __buscaBinRec(self, chave, ini, fim, vet):
        meio = (ini + fim) // 2  # Arredondando para baixo
        if ini > fim or ini < 0 or fim < 0:
            return -1
        if vet[meio] == chave:
            return meio
        elif vet[meio] < chave:
            return self.__buscaBinRec(chave, meio+1, fim, vet)
        return self.__buscaBinRec(chave,ini, meio-1 ,vet)


tabela = Table(7)
tabela.inserirOrd("chave1","oi")
print(tabela.chave)
print("-->")
tabela.inserirOrd("chave2","tchau")
print(tabela.chave)
print("-->")
tabela.inserirOrd("chave8","tchauuuuu")
print(tabela.chave)
tabela.inserirOrd("chave5","tchauuuuu")
print(tabela.chave)
tabela.inserirOrd("chave-1","tchauuuuu")
print(tabela.chave)
tabela.inserirOrd("au","tchauuuuu")
print(tabela.chave)
print(tabela.buscaLinearRec("au"))
print(tabela.buscarBinariaRecursiva("au"))