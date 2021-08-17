from Produto import Produto

p1 = Produto(10)

p1.preco = 19.9
p1.nome = 'iPhone'

print(f"Novo preço do {p1.nome} - {p1.preco}")
print(p1.aumentarPreco(20))

print('-------\n')
p1.imprimir()