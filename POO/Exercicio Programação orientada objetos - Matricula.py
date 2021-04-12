class Livro:

	def __init__(self, titulo, autor, num_paginas):
		self.titulo = titulo
		self.autor = autor
		self.num_paginas = num_paginas

# Programa principal:
livro1 = Livro('Introdução à Programação em Python', 'Fulano de Tal', 350)
livro2 = Livro('Matemática Financeira', 'José da Silva', 178)

print('Informações dos livros:')
print('Titulo:', livro1.titulo, '  /  Autor:', livro1.autor, '  /  Num págs:', livro1.num_paginas)
print('Titulo:', livro2.titulo, '  /  Autor:', livro2.autor, '  /  Num págs:', livro2.num_paginas)

