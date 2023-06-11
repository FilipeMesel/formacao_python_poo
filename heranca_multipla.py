class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        # return(f"Biscicleta {self.modelo} de cor {self.cor} cujo ano é {self.ano} e custa R${self.valor},00")


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo

class Ave(Animal):
    #Usando o conceito de key words para pegar atributos da classe pai
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico

class Gato(Mamifero):
    pass

class Ornintorrinco(Mamifero, Ave):
    def __init__(self, nro_patas, cor_pelo, cor_bico):
        super().__init__(nro_patas = nro_patas, cor_pelo = cor_pelo, cor_bico = cor_bico)
        print(Ornintorrinco.__mro__)

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        # return(f"Biscicleta {self.modelo} de cor {self.cor} cujo ano é {self.ano} e custa R${self.valor},00")



gato = Gato(nro_patas = 4, cor_pelo="caramelo")
ornintorrinco = Ornintorrinco(nro_patas = 4, cor_pelo="caramelo", cor_bico="azul")
print(gato)
print(ornintorrinco)