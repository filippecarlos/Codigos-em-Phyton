class Bomba:

  def __init__(self, peso):
      self.peso = peso
  
  def explodir (self):
    i=0
    while i < self.peso:
      print ('BOMMMMMM!')
      i +=1

class Relogio:
  def __init__(self, hora, minuto) -> None:
      self.hora = hora
      self.minuto = minuto
  
  def tick(self):
    self.minuto +=1
    if self.minuto >59:
      self.minuto = 0
      self.hora +=1
      if self.hora > 23:
        self.hora = 0

class BombaRelogio (Bomba, Relogio):

  def __init__(self, peso, hora, minuto, hora_explosao, minuto_explosao):
      Bomba.__init__ (self, peso)
      Relogio.__init__ (self, hora, minuto)
      self.hora_explosao = hora_explosao
      self.minuto_explosao = minuto_explosao
      self.tensao_fio_amarelo = 0

  def cortar_fio_amarelo (self):
    self.tensao_fio_amarelo = 0 
  
  def ligar_fio_amarelo (self):
    self.ligar_fio_amarelo = 5

  def tick (self):
    Relogio.tick (self)
    if self.hora == self.hora_explosao and self.minuto == self.minuto_explosao and self.tensao_fio_amarelo == 5:
      Bomba.explodir(self)

# Program Principal

bomba_relogio = BombaRelogio (3, 10, 5, 10, 10)
bomba_relogio.ligar_fio_amarelo()
for i in range (10):
  print ('Hora atual: , %02d:%02d' % (bomba_relogio.hora, bomba_relogio.minuto))
  bomba_relogio.tick()

