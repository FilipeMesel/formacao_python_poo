class Foo:
    def __init__(self, x = None):
        self._x = x

    #Nesse caso, "x" não é um método, é uma propriedade
    @property
    def x(self):
        return self._x or 0

    #Veja agora como setar o atributo x:
    @x.setter
    def x(self, value):
        self._x += value
    
    #veja como deletar o atributo x:
    @x.deleter
    def x(self):
        #Isso aqui deletaria o atributo 
        # del self._x
        self._x = -1

foo = Foo(10)
print(foo.x)
foo.x = 10
print(foo.x)
del foo.x
print(foo.x)