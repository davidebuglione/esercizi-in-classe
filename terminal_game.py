#creazione classe entity
class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #funzione per muovere un'entità
    def move(self, direction):
        if direction == "w"  and self.y > 0:
            self.y -= 1
        elif direction == "s" and self.y < field.h - 1:
            self.y += 1
        elif direction == "d" and self.x < field.w - 1:
            self.x +=1
        elif direction == "a" and self.x > 0:
            self.x -= 1

#creazione classe Field
class Field:
    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.entities = []

    #funzione per disegnare il campo di gioco
    def draw_field(self):
        for y in range(self.h):
            for x in range(self.w):
                for e in self.entities:
                    if y == e.y and x == e.x:
                        print('[X]', end = '')
                        break

                else:
                    print('[ ]', end = '')
            print()

#richiesta misure campo all'utente
h_field = int(input("inserire l'altezza del campo"))
w_field = int(input("inserire la larghezza del campo"))
field = Field(h_field, w_field)

entity = Entity(2,3)
field.entities.append(entity)

#ciclo di gioco
while True:
    field.draw_field()
    move = input("inserire un comando di movimento ").lower()
    if move == "stop":
        quit()
    entity.move(move)