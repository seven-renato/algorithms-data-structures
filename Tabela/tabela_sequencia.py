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
        
    def buscar(self, chave):
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


    def inserir(self, chave, valor):
        if self.vazia():
            self.ini = 1
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
                self.valor[self.ini+self.tamanho()] = valor
                self.chave[self.ini+self.tamanho()] = chave
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

tabela = Table(5)

tabela.inserir("AAAA1132", "chrevolet")



tabela.inserir("AAAA1134", "chrevwadawdolet")


tabela.inserir("AAAA1134", "arrozinho")

tabela.inserir("AAAA1134", "arroz")

tabela.inserir("BBB1134", "chocolate")

tabela.inserir("CCCC1134", "pedra")

tabela.inserir("DDDD1134", "pau")

tabela.inserir("EEEE1134", "fim")

print(tabela.chave)
print(tabela.valor)

tabela.remover("BBB1134")
print(tabela.chave)
print(tabela.valor)
tabela.inserir("EEEE1134", "caminho")
print(tabela.chave)
print(tabela.valor)
tabela.remover("EEEE1134")
print(tabela.chave)
print(tabela.valor)
print(tabela.consultar("DDDD1134"))

tabela.remover("AAAA1132")
print(tabela.chave)
print(tabela.valor)