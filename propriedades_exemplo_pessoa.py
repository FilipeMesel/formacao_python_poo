class Pessoa:
    def __init__(self, name, ano_nascimento):
        self.name = name
        self._ano_nascimento = ano_nascimento
    
    @property
    def idade(self):
        _ano_atual = 2023
        return 2023 - self._ano_nascimento

pessoa = Pessoa("Filipe", 1996)
print(pessoa.name)
print(pessoa.idade)