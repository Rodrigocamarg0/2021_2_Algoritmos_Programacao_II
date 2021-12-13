from No import No
from Livro import Livro

class Fila:

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def adicionar(self, valor: Livro):
        no = No( valor )
        if self.tamanho == 0:
            self.inicio = no
            self.fim = no
        else:
            self.fim.proximo = no
            self.fim = no
        self.tamanho += 1



    def imprimir(self):
        if self.inicio == None :
            print("Fila Vazia!")
        else:
            aux = self.inicio
            while ( aux ) :
                aux.dado.imprimir()
                aux = aux.proximo


    def remover(self):
        if self.tamanho == 0:
            print( "Fila Vazia!")
        elif self.tamanho == 1:
            self.inicio = None
            self.fim = None
            self.tamanho = 0
        else:
            self.inicio = self.inicio.proximo
            self.tamanho -= 1
