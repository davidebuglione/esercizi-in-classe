#Crea una classe Quadrato con l'attributo lato e i metodi per il clacolo del perimetro e dell'area

class Quadrato():
    def __init__(self, lato):
        self.lato=lato
    def get_perimeter(self):
        print("Il perimetro è", self.lato*4)
    def get_area(self):
        print("l'area è", self.lato**2)