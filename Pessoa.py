# Classe PESSOA
#CLasse PESSOA FISICA
#CLASSE PESSOA JURIDICA




#ENDERECO
# 
# 

from datetime import date


class Endereco():
    def __init__(self,logradouro ="",numero ="",endereco_Comercial=False):
        #inicializar os nossos atributos com valores padrao
     self.logradouro = logradouro
     self.numero = numero
     self.endereco_Comercial = endereco_Comercial 


# Classe PESSOA

class Pessoa():
    def __init__(self,nome="",rendimento=0.0,endereco=None):
        self.nome = nome
        self.rendimento = rendimento
        self.endereco = endereco
    
    def calcular_imposto(self,rendimento):
        return rendimento


#CLasse PESSOA FISICA

class PessoaFisica(Pessoa):
    #inicializar os atributos que foram herdados e proprios atributos da classe
    def __init__(self, nome="", rendimento=0, endereco=None, cpf="",dataNasciemnto="",):
        if endereco is None:
            #se nenhum endereco for fornecido, cria um objeto endereco padrao 
            endereco = Endereco()
        if dataNasciemnto is None:
            dataNasciemnto = date.today()

        super().__init__(nome,rendimento,endereco)
        #Chama o construtor da super classe pessoa para inicializar os atributos herdados
        
        
        #atributos da propria classe
        self.cpf = cpf
        self.dataNascimento= dataNasciemnto
    
    def calcular_imposto(self, rendimento:float) -> float:
        if rendimento <= 1500:
             return 0
        elif 1500 < rendimento <= 3500:
         return (rendimento/100)*2
                
        elif 3500 < rendimento <= 6000:
            return (rendimento/100)*3.5
        else:
           return (rendimento/100)*0.5
        
        
        
    


    
       


#CLASSE PESSOA JURIDICA
class PessoaJuridica(Pessoa):
    def __init__(self,nome="",rendimento=0,endereco=None,cnpj=""):
     if endereco is None:
            #se nenhum endereco for fornecido, cria um objeto endereco padrao 
            endereco = Endereco()

        
     super().__init__(nome,rendimento,endereco)
     self.cnpj = cnpj
     

    def calcular_imposto(self, rendimento:float) -> float:
        if rendimento <= 1500:
             return 0
        elif 1500 < rendimento <= 3500:
         return (rendimento/100)*2
                
        elif 3500 < rendimento <= 6000:
            return (rendimento/100)*3.5
        else:
           return (rendimento/100)*0.5
  





    