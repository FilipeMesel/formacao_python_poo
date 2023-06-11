class Ave:
    def voar(self):
        print("voando...")

class Pardal(Ave):
    def voar(self):
        super().voar()

class Avestruz(Ave):
    def voar(self):
        print("Avestruz não voa")

#Uma loucura pois "Avião" na vida real não é filho de Ave
class Aviao(Ave):
    def voar(self):
        print("Decolando...")

def plano_de_voo(obj):
    obj.voar()

pardal = Pardal()
avestruz = Avestruz()
plano_de_voo(pardal)
plano_de_voo(avestruz)
plano_de_voo(Aviao())