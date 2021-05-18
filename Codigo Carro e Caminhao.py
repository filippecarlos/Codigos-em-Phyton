class Motor:
  def __init__(self, cilindrada, potencia):
      self.cilindrada = cilindrada
      self.potencia = potencia  

class Veiculo:
  def __init__(self, ano, preco, motor):
      self.ano = ano
      self.preco = preco
      self.motor = motor
  
  def exibir_dados(self):
    print('Dados do veiculo: ')
    print('   Ano de fabricação: ', self.ano)
    print('   Preço: ', self.preco)
    print('   Cilindrada do motor: ', self.motor.cilindrada)
    print('   Potencia do motor: ', self.motor.potencia)

class Carro(Veiculo):
  def __init__(self, ano, preco, motor, cor, modelo):
      super().__init__(ano, preco, motor)
      self. cor = cor
      self.modelo = modelo
  
  def exibir_dados(self):
      super().exibir_dados()
      print('   Cor: ', self.cor)
      print('   Modelo: ', self.modelo)

class Caminhao(Veiculo):
  def __init__(self, ano, preco, motor, comprimento):
      super().__init__(ano, preco, motor)
      self.comprimento = comprimento
  
  def exibir_dados(self):
      super().exibir_dados()
      print ('    Comprimento: ', self.comprimento)

#programa principal

motor1 = Motor (1000,500)
motor2 = Motor (700,590)

carro = Carro (2010, 20000, motor1, 'Branco', 'Gol')
caminhao = Caminhao (2009, 50000, motor2, 10)

carro.exibir_dados()
caminhao.exibir_dados()

