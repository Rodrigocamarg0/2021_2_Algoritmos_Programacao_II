from Autor import Autor

class Livro:
    def __init__(self, id, titulo, autor: Autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor

    def imprimir(self):
        print(f'======== Livro =======')
        print(f'ID Livro:     {self.id}')
        print(f'Título:    {self.titulo}')
        print(f'{self.autor.imprimirAutor()}')
    
        