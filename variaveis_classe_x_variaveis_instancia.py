class Estudante:
    #Variavel de classe
    escola = "DIO"

    def __init__(self, nome, matricula):
        #Variaveis de instância
        self.nome = nome
        self.matricula = matricula
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        # return(f"Biscicleta {self.modelo} de cor {self.cor} cujo ano é {self.ano} e custa R${self.valor},00")

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

mesels = Estudante("Filipe", 1234)
fulano = Estudante("Fulano", 4321)

mostrar_valores(mesels, fulano)