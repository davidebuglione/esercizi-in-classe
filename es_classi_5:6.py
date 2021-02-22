'''
-elenca proprietà e metodi della classe prodotto
-definisci il metodo assegna_prezzo alla classe Prodotto
'''

class Prodotto:
    def __init__(self, name, price=0):
        self.name=name
        self.price=price
    def input_price(self, new_price):
        self.price=new_price
