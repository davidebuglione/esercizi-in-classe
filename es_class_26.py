class Triangolo():
    def __init__(self, lato1, lato2, lato3, altezza):
        self.lato1=lato1
        self.lato2=lato2
        self.lato3=lato3
        self.altezza=altezza
    def get_perimetro(self):
        self.perimetro=self.lato1+self.lato2+self.lato3
class TriangoloIsoscele(Triangolo):
    self.lato_uguale=lato2
class TriangoloEquilatero(TriangoloIsoscele):
    def __init__(self):
        self.lato=lato
tr1=Triangolo(3,4)