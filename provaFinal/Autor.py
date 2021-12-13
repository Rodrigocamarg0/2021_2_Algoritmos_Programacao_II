class Autor:
    def __init__(self, id, nome):
        self.__id = id
        self.nome = nome
    def imprimirAutor(self):
        print(f'Autor: {self.nome}')
        print(f'ID Autor:    {self.__id}')