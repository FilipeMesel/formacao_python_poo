class Pessoa:
    #Construtor
    def __init__(self, nome= None, idade = None):
        self.nome = nome
        self.idade = idade

    #Métodos de classe: Mexem diretamente com dados da classe
    @classmethod
    def criar_de_data_nascimento(cls, nome, ano, mes, dia):
        idade = 2023 - ano
        #CLS = Referência para a classe
        return cls(nome, idade)

    #Métodos estáticos: Alteram o valor de objetos
    #Não precisa nem do contexto da classe e nem do contexto do objeto.
    @staticmethod
    def e_maior_idade(idade):

        return idade >= 18
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        # return(f"Biscicleta {self.modelo} de cor {self.cor} cujo ano é {self.ano} e custa R${self.valor},00")

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)
    

p1 = Pessoa("Filipe", 27)
p2 = Pessoa.criar_de_data_nascimento("Filipe", 1996, 10, 14)

mostrar_valores(p1, p2)
print(Pessoa.e_maior_idade(18))


    
