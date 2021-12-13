from typing import List, Any
from copy import deepcopy


class No:
    def __init__(self,valor):
        self.dado = valor
        self.proximo = None

class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

        

    def adicionar(self, valor):
        no = No(valor)
        if self.topo == None:
            self.topo = no
        else:
            no.proximo = self.topo
            self.topo = no
        self.tamanho += 1

    def empilhar(self, valor):
        no = No(valor)
        if self.topo != None:
            no.proximo = self.topo
        self.topo = no
        self.tamanho += 1
    
    def imprimir(self):
        if self.topo == None:
            print("Pilha vazia!")
        else:
            aux = self.topo
            while aux:
                print(aux.dado)
                aux = aux.proximo
            print("--------------------Tamanho: ", self.tamanho)

    def remover(self):
        if self.topo == None:
            print
        elif self.tamanho == 1:
            self.topo = None
            self.tamanho = 0
        else:
            self.topo = self.topo.proximo
            self.tamanho -= 1
        self.imprimir()
       



if __name__ == "__main__":
   pi = Pilha()
   pi.adicionar("Doblo")
   pi.adicionar('Uno')
   pi.adicionar('Toro')
   pi.adicionar('Fusca')

   pi.remover()

   pi.imprimir()