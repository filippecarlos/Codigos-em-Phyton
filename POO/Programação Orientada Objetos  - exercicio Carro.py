
class Produto:

	def __init__(self, nome, preco, quantidade):
		self.nome = nome
		self.preco = preco
		self.quantidade = quantidade


class Pedido:

	def __init__(self):
		self.produtos = []
	
	def adicionar_produto(self, produto):
		self.produtos.append(produto)
	
	def calcular_valor(self):
		total = 0
		for prod in self.produtos:
			total += (prod.preco * prod.quantidade)
		return total

	"""
# Comentado: outra forma de construir o método calcular_valor().
# Você também pode usar essa mesma lógica para trocar o loop for pelo while.
	def calcular_valor(self):
		total = 0
		for i in range(len(self.produtos)):
			total = total + (self.produtos[i].preco * self.produtos[i].quantidade)
		return total
	"""

# Programa principal:
cafe = Produto('Café Solúvel', 5.50, 1)
arroz = Produto('Arroz Integral', 4.90, 2)
feijao = Produto('Feijão Preto', 2.80, 2)
meu_pedido = Pedido()
meu_pedido.adicionar_produto(cafe)
meu_pedido.adicionar_produto(arroz)
meu_pedido.adicionar_produto(feijao)
print('O valor total é:', meu_pedido.calcular_valor())


