class Triangolo():

    def __init__(self, lato1, lato2, lato3, altezza):
        self.lato1 = lato1
        self.lato2 = lato2
        self.lato3 = lato3
        self.altezza = altezza

class TriangoloIsoscele(Triangolo):

    def __init__(self, lato1, lato3, altezza):
        self.lato2=lato1
        super().__init__(lato1, lato3, altezza)

class TriangoloEquilatero(TriangoloIsoscele, Triangolo):
    def __init__(self, lato3, altezza):
        self.lato2=self.lato3
        super().__init__(lato3, altezza)
    def get_perimetro(self):
        self.perimetro = self.lato1+self.lato2+self.lato3
        print(self.perimetro)
Prova= TriangoloEquilatero(4, 7)
Prova.get_perimetro()