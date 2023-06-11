class Conta:
    def __init__(self, nro_agencia, saldo = 0):
        #Quando tem underline antes do nome, convenciona-se que o método é privado
        #E não deve ser usado fora da classe
        self._saldo = saldo
        self.nro_agencia = nro_agencia
    
    def depositar(self, valor):
        self._saldo += valor
    
    def sacar(self, valor):
        self._saldo -= valor
    
    def mostrar_saldo(self):
        return self._saldo

conta1 = Conta("001", 100)
conta1.depositar(200)
conta1.sacar(50)

#Isso aqui deve ser evitado pois "_saldo" é privado e só deve ser usado dentro da classe
print(conta1._saldo)
#Isso aqui pode ser feito
print(conta1.mostrar_saldo())
#Isso aqui pode ser feito porque "nro_agencia" é um atributo público
print(conta1.nro_agencia)