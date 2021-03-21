class Motociclo():
    def __init__(self, n_ruote, n_posti, cilindrata):
        self.n_ruote = n_ruote
        self.n_posti = n_posti
        self.cilindrata = cilindrata
    def info(self):
        print(self.n_ruote, self.n_posti, self.cilindrata, end=" ")

class Ciclomotore(Motociclo):
    def __init__(self, colore, n_ruote, n_posti, cilindrata, cambio_manuale=True):
        super().__init__(n_ruote, n_posti, cilindrata)
        self.cambio_manuale = cambio_manuale
        self.colore= colore
    def complete_info(self):
        super().info()
        print(self.cambio_manuale, self.colore)