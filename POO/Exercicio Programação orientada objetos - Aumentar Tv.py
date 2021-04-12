class Televisao:

	def __init__(self):
		self.canal = None
		self.volume = 0
	
	def aumentar_volume(self):
		self.volume += 1
		if self.volume > 100:
			self.volume = 100
	
	def diminuir_volume(self):
		self.volume -= 1
		if self.volume < 0:
			self.volume = 0
	
	def alterar_canal(self, num_canal):
		self.canal = num_canal

# Programa principal:
tv = Televisao()
tv.alterar_canal(12)
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.diminuir_volume()
print('A TV está no canal:', tv.canal)  # imprime: A TV está no canal 12
print('A TV está no volume:', tv.volume)  # imprime: A TV está no volume 2