class Televisao: 
          def __init__(self):
                    self.canal = None
                    self.volume = 0
          def aumentar_volume (self):
                    self.volume+=1
                    if self.volume > 100:
                              self.volume = 100
                              
          def dimunuir_volume(self):
                    self.volume -=1
                    if self.volume <0:
                              self.volume = 0
                              
          def alterar_canalysis(self, num_canal):
                    self.num_canal = num_canal
                    
# PRograma Principal
tv= Televisao()
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
print('A TV está no canal: ' , tv.canal)
print('A Tv esta no volume: ', tv.volume)
                    
                                        