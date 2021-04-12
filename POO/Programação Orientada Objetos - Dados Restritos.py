class Pessoa:
          def __init__ (self, nome, idade, cpf, rg): # criação de atributos
                    self.nome = nome
                    self.idade = idade
                    self.__cpf = cpf
                    self.__rg = rg
          
          #get (Devolve o valor solicitado)
          def get_cpf (self):
                    return self.__cpf
          
          def get_rg (self):
                    return self.__rg
          
          #set (Recebe e Altera o valor do atributo)
          def set_cpf (self, novo_cpf):
                    self.__cpf = novo_cpf
                    
          def set_rg (self, novo_rg):
                    self.__rg = novo_rg
                    

#programa principal
                                     
pessoa = Pessoa ('Bia', 19, 1561651561, 55456160)
print ('cpf', pessoa.get_cpf())
print ('Rg', pessoa.get_rg())

pessoa.set_cpf (101012)
pessoa.set_rg (222222)

print ('Novo cpf', pessoa.get_cpf())
print ('Novo Rg', pessoa.get_rg())




                    