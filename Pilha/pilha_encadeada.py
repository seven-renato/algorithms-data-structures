class Nodo:
    def __init__(self, info):
        self.info = info
        self.prox = None

class PilhaEncadeada:
    def __init__(self):
        self.topo = None

    def vazia(self):
        if self.topo == None:
            return True
        return False

    def empilhar(self, dado):
        novo = Nodo(dado)
        if (not self.vazia()):
            novo.prox = self.topo
        self.topo = novo

    def excluir(self):
        if(not self.vazia()):
            self.topo = self.topo.prox
            # aux = self.topo
            # self.topo = aux.prox
            # del aux // excluir da memória

    def consultar(self):
        if(not self.vazia()):
            return self.topo.info
        
    def destruir(self):
        while(not self.vazia()):
            self.excluir()