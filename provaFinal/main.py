from Fila import Fila
from Livro import Livro
from Autor import Autor


Jk_Rowling = Autor(id = 1, nome='Joanne Rowling')

HP_PF = Livro(1,'Harry Potter e a Pedra Filosofal', Jk_Rowling)
HP_CS = Livro(2,'Harry Potter e a Câmara Secreta', Jk_Rowling)
HP_PA = Livro(3,'Harry Potter e o Prisioneiro de Azkaban', Jk_Rowling)
HP_CF = Livro(4,'Harry Potter e o Cálice de Fogo', Jk_Rowling)

f1 = Fila()

f1.adicionar( HP_PF )
f1.adicionar( HP_CS )
f1.adicionar( HP_PA )

f1.imprimir()


f1.remover()

f1.adicionar( HP_CF )


f1.imprimir()

f1.remover()


f1.remover()

f1.remover()