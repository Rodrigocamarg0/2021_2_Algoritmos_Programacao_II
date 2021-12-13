from abc import abstractmethod


class Ferramenta:
  def __init__(self,nome,tensao,preco):
    self.nome = nome
    self.tensao = tensao
    self.preco = preco
  
  def getInformacoes(self):
    print(f"Nome: {self.nome}")
    print(f"Tensão: {self.tensao}")
    print(f"Preço: R${self.preco}")

  @abstractmethod
  def cadastrar(self):
      pass
