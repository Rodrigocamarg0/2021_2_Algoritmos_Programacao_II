class Produto:
    def __init__(self, qtd):
        self.nome = input("Digite o nome do Produto: ")
        self.preco = 0
        self.quantidade = qtd
    def imprimir(self):
        print(f'Nome: {self.nome}')
        print(f'Preço: {self.preco}')
        print(f'Quantidade: {self.quantidade}')
    def aumentarPreco(self, percent):
        self.preco += self.preco * percent / 100
        return self.preco