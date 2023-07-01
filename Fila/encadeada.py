class Nodo:
    def __init__(self, info):
        self.info = info
        self.prox = None

class FilaEnc:
    def __init__(self):
        self.ini = None
        self.fim = None
    
    def vazia(self):
        if self.ini == None and self.fim == None:
            return True
        return False

    def consultar (self):
        if not self.vazia():
            return self.ini.info
        
    def inserir(self, dado):
        novo = Nodo(dado)
        if self.vazia():
            self.ini = novo
        else:
            self.fim.prox = novo
        self.fim = novo

    def excluir(self):
        if (not self.vazia()):
            self.ini = self.ini.prox
        else:
            self.fim = None
    
    def destruir(self):
        while (not self.vazia()):
            self.excluir()