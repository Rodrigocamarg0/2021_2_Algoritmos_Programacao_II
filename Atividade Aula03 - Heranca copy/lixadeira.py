from ferramenta import Ferramenta

class Lixadeira(Ferramenta):
  def __init__(self,nome, tensao, preco, rotacoes):
    super().__init__(nome, tensao, preco)
    self.__rotacoes = rotacoes

  def getInformacoes(self):
    Ferramenta.getInformacoes(self)
    print(f"Rotações: {self.__rotacoes}")
  
  def cadastrar():
    nome = input("Informe o nome: ")
    tensao = input("Informe a tensao: ")
    preco = input("Informe o Preço: ")
    rotacoes = input("Informe o Rotações: ")

    objeto = Lixadeira(nome,tensao, preco, rotacoes) 
    return objeto