class PilhaContigua:
    def __init__(self, tamanho):
        self.vetor = [None]*tamanho
        self.lim = tamanho - 1
        self.base = 0
        self.topo = self.base - 1

    def empilhar(self, dado):
        if (self.topo < self.lim):
            self.topo += 1
            self.vetor[self.topo] = dado

    def excluir(self):
        if (self.topo >= self.base):
            self.topo -= 1

    def consultar(self):
        if (self.topo >= self.base):
            return self.vetor[self.topo]
    
    def destruir(self):
        self.topo = self.base -1    