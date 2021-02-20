class Atleta:
    def __init__(self, name, squad_name, visitaMedica=False):
        self.name=name
        self.squad_name=squad_name
        self.visitaMedica=visitaMedica
    def effettua_visita(self):
        self.visitaMedica=True
    def info(self):
        if self.visitaMedica==True:
            print(self.name,"ha eseguito con successo la visita medica")
        else:
            print(self.name,"non ha ancora eseguitp la visita medica")
        print("...e gioca nella seguente squadra:", self.squad_name)