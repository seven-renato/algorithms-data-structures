from carro import *
from contigua import *
from encadeada import *


f = FilaCont(3) 
#f = FilaEnc()

#print(f.consultar())
#print(f)
f.inserir(Carro("AAAAAA111", 1111))
#print(f.consultar())
f.inserir(Carro("BBBBB222", 2222))
#print(f.consultar())
f.inserir(Carro("CCC33333", 3333))
#print(f.consultar())

f.excluir()
#print(f.consultar())

f.excluir()
#print(f.consultar())

f.inserir(Carro("DDDD44444", 3333))
#print(f.consultar())

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

    def imprimir(self):
        teste = PilhaEncadeada()
        teste.topo = self.topo
        while not teste.vazia():
            print(teste.consultar())
            teste.excluir()




def ordenar(fila):
    if not fila.vazia():
        pilha1 = PilhaEncadeada()            
        pilha2 = PilhaEncadeada()
        valor_atual = fila.consultar()
        pilha1.empilhar(valor_atual)
        fila.excluir()
        valor_atual = fila.consultar()
        while valor_atual != None:
            if valor_atual <= pilha1.consultar():
                pilha1.empilhar(valor_atual)
            else:
                while pilha1.consultar() != None:
                    if pilha1.consultar() >= valor_atual:
                        pilha1.empilhar(valor_atual)
                        break
                    else:
                        pilha2.empilhar(pilha1.consultar())
                        pilha1.excluir()
                if pilha1.consultar() == None:
                    pilha1.empilhar(valor_atual)
                while pilha2.consultar() != None:
                    pilha1.empilhar(pilha2.consultar())
                    pilha2.excluir()
            fila.excluir()
            valor_atual = fila.consultar()
        return pilha1            

filateste = FilaCont(10)
filateste.inserir(3)
filateste.inserir(6)
filateste.inserir(5)
filateste.inserir(2)
filateste.inserir(4)
filateste.inserir(1)
filateste.inserir(2)

print(filateste.vetor)


teste = (ordenar(filateste))
teste.imprimir()


            #     pilha2.empilhar(pilha1.consultar())
            #     pilha1.excluir()
            # pilha1.empilhar(valor_atual)
            # while pilha2.consultar() != None:
            #     pilha1.empilhar(pilha2.consultar())
            #     pilha2.excluir()