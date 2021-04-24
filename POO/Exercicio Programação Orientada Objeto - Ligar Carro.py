import sys
from io import StringIO
import re
import unicodedata
import traceback
if __name__ != '__main__': # NÃO EDITE ESSA LINHA
	input = lambda x: 10  # NÃO EDITE ESSA LINHA
"""
O código acima serve para testar o seu programa. Alterá-lo prejudicará
a correção da sua atividade e consequentemente a sua nota! 
"""
## ===================================================================
## ===================================================================

# INFORME SEUS DADOS (como string nas variáveis a seguir):
NUMERO_RA = "1904750"
NOME_COMPLETO = "Filippe Carlos Valadão de Freitas "
# OBS: Não informar seus dados corretamente implicará em nota 0.0 (zero)!

# CONSTRUA O SEU PROGRAMA A PARTIR DAQUI:

class Carro:
          def __init__ (self,modelo,cor):
                  self.modelo=modelo
                  self.cor=cor
                  self.km_rodados=0
                  self.ligado=False

          def ligar (self):
                  self.ligado=True                   

          def desligar (self):
                  self.ligado=False                    
          
          def mover(self, km):
                  if self.ligado == True:
                          self.km_rodados += km
                    
          def exibir (self):
                  print (self.modelo)
                  print (self.cor)
                  print (self.km_rodados)
                  print (self.ligado)
    

# Programa principal sugerido para chamar a sua função e testar o seu código.
# Você pode alterá-lo se desejar, mas isso não é obrigatório.
def programa_principal():
	try:
		carro = Carro('Fusca', 'Azul')   # cria um novo carro, passando o modelo e a cor como parâmetros para o construtor
		carro.mover(30)  # não adiciona nada aos km_rodados, pois ligado é False
		carro.ligar()    # muda o atributo ligado para True
		carro.mover(12)  # adiciona 12 aos km_rodados, pois o carro está ligado
		carro.desligar() # muda o atributo ligado para False
		carro.exibir()   # imprime as informações do carro, conforme o comentário de múltiplas linhas abaixo:
		"""
		Fusca
		Azul
		12
		False
		"""
	except:
		pass
programa_principal()







## ===================================================================
## ===================================================================
# NÃO EDITE O CÓDIGO A PARTIR DESTE PONTO:
"""
O código abaixo serve para testar o seu programa. Alterá-lo prejudicará
a correção da sua atividade e consequentemente a sua nota! 
"""

if __name__ == '__main__': # NÃO EDITE ESSA LINHA

	class TesteClasseV2:
		def __init__(self, nome_teste, classe, lista_param_init, tipo_teste, saida_esperada, 
			nome_attr, valor_attr, nome_metodo, lista_param_metodo, modificar_attrs={}):
			self.nome_teste = nome_teste
			self.classe = classe
			self.lista_param_init = lista_param_init
			self.tipo_teste = tipo_teste.upper()
			self.saida_esperada = str(saida_esperada)
			self.nome_attr = nome_attr
			self.valor_attr = valor_attr
			self.nome_metodo = nome_metodo
			self.lista_param_metodo = lista_param_metodo
			self.modificar_attrs = modificar_attrs # atributos que devem ter seus valores modificados após instanciar o objeto

			self.saida_obtida = ''
			self.passou = False
		
		def formata_saida(self, s):
			s = ''.join(c for c in unicodedata.normalize('NFD', s)
					if unicodedata.category(c) != 'Mn') # remove acentos
			s = re.sub('\s+', '', s)
			s = s.strip('!')
			s = s.strip('?')
			s = s.strip('.')
			return s.upper()
		
		def inicializa_atributos(self, instancia_classe):
			for nome_atributo in self.modificar_attrs:   # modifica o valor de alguns atributos após inicializar a classe
				setattr(instancia_classe, nome_atributo, self.modificar_attrs[nome_atributo])
		
		def testa_cria_instancia(self):
			try:
				instancia = self.classe(*self.lista_param_init)
				return True
			except:
				return False

		def testa_atributo_inicializado(self):
			try:
				instancia = self.classe(*self.lista_param_init)
				valor = getattr(instancia, self.nome_attr)
				self.saida_obtida = str(valor)
				if self.saida_obtida == self.saida_esperada:
					return True
				else:
					return False
			except:
				return False
		
		def testa_atributo_apos_metodo(self):
			try:
				instancia = self.classe(*self.lista_param_init)
				self.inicializa_atributos(instancia)
				#for nome_atributo in self.modificar_attrs:   # modifica o valor de alguns atributos após inicializar a classe
				#	setattr(instancia, nome_atributo, self.modificar_attrs[nome_atributo])
				setattr(instancia, self.nome_attr, self.valor_attr) # modifica o atributo antes, para verificar se o método o modifica após ser chamado
				metodo = getattr(instancia, self.nome_metodo)
				metodo(*self.lista_param_metodo)
				valor = getattr(instancia, self.nome_attr)
				self.saida_obtida = str(valor)
				if self.saida_obtida == self.saida_esperada:
					return True
				else:
					return False
			except:
				return False
		
		def testa_metodo_apos_atributo(self):
			try:
				instancia = self.classe(*self.lista_param_init)
				self.inicializa_atributos(instancia)
				setattr(instancia, self.nome_attr, self.valor_attr)
				metodo = getattr(instancia, self.nome_metodo)
				resultado = metodo(*self.lista_param_metodo)
				self.saida_obtida = str(resultado)
				if self.saida_obtida == self.saida_esperada:
					return True
				else:
					return False
			except:
				return False

		def testa_prints_metodo(self):
			saida = ''
			try:
				OLD_STDOUT = sys.stdout
				sys.stdout = NEW_STDOUT = StringIO()
				instancia = self.classe(*self.lista_param_init)
				self.inicializa_atributos(instancia)
				metodo = getattr(instancia, self.nome_metodo)
				metodo(*self.lista_param_metodo)
			except:
				pass
			finally:
				sys.stdout = OLD_STDOUT
				saida = NEW_STDOUT.getvalue().strip()		
				self.saida_obtida = saida
			if self.formata_saida(saida) == self.formata_saida(self.saida_esperada):
				return True
			else:
				return False
		
		def testa_return_metodo(self):
			saida = None
			try:
				instancia = self.classe(*self.lista_param_init)
				self.inicializa_atributos(instancia)
				metodo = getattr(instancia, self.nome_metodo)
				if len(self.lista_param_metodo) > 0:
					saida = metodo(*self.lista_param_metodo)
				else:
					saida = metodo()
				self.saida_obtida = str(saida)
			except:
				pass
			if self.saida_obtida == self.saida_esperada:
				return True
			else:
				return False

		def execute(self):
			if self.tipo_teste == 'CRIA_INSTANCIA':
				self.passou = self.testa_cria_instancia()
			elif self.tipo_teste == 'ATRIBUTO_INICIALIZADO':
				self.passou = self.testa_atributo_inicializado()
			elif self.tipo_teste == 'ATRIBUTO_APOS_METODO':
				self.passou = self.testa_atributo_apos_metodo()
			elif self.tipo_teste == 'METODO_APOS_ATRIBUTO':
				self.passou = self.testa_metodo_apos_atributo()
			elif self.tipo_teste == 'PRINTS_METODO':
				self.passou = self.testa_prints_metodo()
			elif self.tipo_teste == 'RETURN_METODO':
				self.passou = self.testa_return_metodo()
			return self.passou

		def __repr__(self):
			resultado = 'OK' if self.passou else 'FALHOU'
			return 'Nome do teste: {0}  |  Resultado do teste: {1}  |  Instância: {2}{3}  |  Saída esperada: {4}  |  Saída obtida: {5}'.format(self.nome_teste, resultado, self.nome_classe, tuple(self.lista_param_init), self.saida_esperada, self.saida_obtida.replace('\n', ' '))


	def checks_iniciais(nome, ra):
		if (type(nome) is str) and (type(ra) is str) and nome.strip() != '' and ra.strip() != '':
			if ra.isnumeric():
				return True
			else:
				print('Erro: RA inválido ou o NOME_COMPLETO e NUMERO_RA estão invertidos!')
		else:
			print('Erro: O número de matrícula ou o nome não foram preenchidos ou não são do tipo string!')
		return False

	def run(**kwargs):
		nome = kwargs.get('nome')
		ra = kwargs.get('ra')
		classe = kwargs.get('classe')
		print('\n')
		print("="*50)
		print("Executando os testes automatizados: ")
		print("="*50)
		if not checks_iniciais(nome, ra):
			return
		try:
			acertos, erros = 0, 0
			lista_testes = [
				TesteClasseV2('Cria instância', classe, ['Gol', 'Branco'], 'CRIA_INSTANCIA', '', None, None, None, None),
				TesteClasseV2('Existe atributo modelo', classe, ['Gol', 'Branco'], 'ATRIBUTO_INICIALIZADO', 'Gol', 'modelo', None, None, None),
				TesteClasseV2('Existe atributo cor', classe, ['Gol', 'Branco'], 'ATRIBUTO_INICIALIZADO', 'Branco', 'cor', None, None, None),
				TesteClasseV2('Existe atributo km_rodados', classe, ['Gol', 'Branco'], 'ATRIBUTO_INICIALIZADO', '0', 'km_rodados', None, None, None),
				TesteClasseV2('Existe atributo ligado', classe, ['Gol', 'Branco'], 'ATRIBUTO_INICIALIZADO', 'False', 'ligado', None, None, None),
				TesteClasseV2('Método ligar()', classe, ['Gol', 'Branco'], 'ATRIBUTO_APOS_METODO', 'True', 'ligado', False, 'ligar', []),
				TesteClasseV2('Método desligar()', classe, ['Gol', 'Branco'], 'ATRIBUTO_APOS_METODO', 'False', 'ligado', True, 'desligar', []),
				TesteClasseV2('Método mover(km) com o carro desligado', classe, ['Gol', 'Branco'], 'ATRIBUTO_APOS_METODO', '0', 'km_rodados', 0, 'mover', [10]),
				TesteClasseV2('Método mover(km) com o carro ligado', classe, ['Gol', 'Branco'], 'ATRIBUTO_APOS_METODO', '23', 'km_rodados', 5, 'mover', [18], {'ligado':True}),
				TesteClasseV2('Método exibir()', classe, ['Onix', 'Grafite'], 'PRINTS_METODO', 'Onix Grafite 12 True', None, None, 'exibir', [], {'km_rodados':12, 'ligado':True}),
			]
			for teste in lista_testes:
				print('Executando o teste: "{0}" ... '.format(teste.nome_teste), end='')
				if teste.execute():
					acertos += 1
					print('OK!')
				else:
					erros += 1
					print('FALHOU!')
			print(' > Resultado:   Passou em: {0} teste(s)   /  Falhou em: {1} teste(s)'.format(acertos, erros))
		except:
			traceback.print_exc()

	run(nome=NOME_COMPLETO, ra=NUMERO_RA, classe=Carro)

