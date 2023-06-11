class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligar_motor(self):
        print("Ligando o motor")
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        # return(f"Biscicleta {self.modelo} de cor {self.cor} cujo ano é {self.ano} e custa R${self.valor},00")


class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        if(self.carregado == False):
            print("Não estou carregado")
        else:
            print("Estou carregado")


Moto1 = Motocicleta("Vermelha", "ABC-123", 2)
Moto1.ligar_motor()

caminhao1 = Caminhao("Vermelha", "ABC-123", 4, True)
caminhao1.ligar_motor()
caminhao1.esta_carregado()

print(Moto1)
print(caminhao1)