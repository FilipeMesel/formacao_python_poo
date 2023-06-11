#Interface define o que a classe deve fazer e NÃO como ela deve fazer
#Não há a palavra reservada "interface" em python. Para isso, usamos classes abstratas que NÃO SÃO INSTANCIADAS
#Python usa o módulo ABC para criar as classes abstratas
from abc import ABC, abstractmethod, abstractproperty

#Criando a interface Controle remoto
#Isso obriga todas as classes filhas a construirem os métodos ligar e desligar
class ControleRemoto(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass
    
    #Forçando a existencia de uma propriedade
    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando TV...")

    def desligar(self):
        print("Desligando TV...")
    
    @property
    def marca(self):
        return "LG"

class ControleARcondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando AR...")

    def desligar(self):
        print("Desligando AR...")
    
    @property
    def marca(self):
        return "SONY"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle2 = ControleARcondicionado()
controle2.ligar()
print(controle2.marca)