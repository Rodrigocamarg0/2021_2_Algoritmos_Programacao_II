from ferramenta import Ferramenta

class Furadeira(Ferramenta):
  def __init__(self, nome, tensao, preco, potencia):
    super().__init__(nome, tensao, preco)
    self.__potencia = potencia

  def getInformacoes(self):
    Ferramenta.getInformacoes(self)
    print(f"Potência: {self.__potencia}")

  def cadastrar():
    nome = input("Informe o nome: ")
    tensao = input("Informe a tensao: ")
    preco = input("Informe o Preço: ")
    potencia = input("Informe o Potência: ")

    objeto = Furadeira(nome,tensao, preco, potencia) 
    return objeto