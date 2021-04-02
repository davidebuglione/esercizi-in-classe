import keyboard
import os
from random import randint

#creazione classe entity
class Entity:
    def __init__(self, x, y):
        self.snake_drawing = "[-]"
        self.x = x
        self.y = y

    #funzione per muovere un'entità
    def move(self, direction):
        futureX = self.x
        futureY = self.y
        if direction == "w"  and self.y > 0:
            futureY -= 1
            self.snake_drawing = "[|]"
        elif direction == "s" and self.y < field.h - 1:
            futureY += 1
            self.snake_drawing = "[|]"
        elif direction == "d" and self.x < field.w - 1:
            futureX += 1
            self.snake_drawing = "[-]"
        elif direction == "a" and self.x > 0:
            futureX -= 1
            self.snake_drawing = "[-]"

        e = field.get_entity_at_coords(futureX, futureY)

        if e == None:
            self.x = futureX
            self.y = futureY
        else:
            self.collide(point)
            self.x = futureX
            self.y = futureY

    def collide(self, entity):
        field.entities.remove(entity)
        return True

#creazione classe snake
class Snake(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)

#creazione classe Field
class Field:
    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.entities = []

#funzione check coordinate future
    def get_entity_at_coords(self, x, y):
        for e in self.entities:
            if e.x == x and e.y == y:
                return e
        return None

    #funzione per disegnare il campo di gioco
    def draw_field(self):
        for y in range(self.h):
            for x in range(self.w):
                for e in self.entities:
                    if e == snake:
                        if y == e.y and x == e.x:
                            print(e.snake_drawing, end="")
                            break
                    else:
                        if y == e.y and x == e.x:
                            print('[X]', end = '')
                            break

                else:
                    print('[ ]', end = '')
            print()

#funzione clearscreen

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#richiesta misure campo all'utente e creazione classi
h_field = int(input("inserire l'altezza del campo"))
w_field = int(input("inserire la larghezza del campo"))
field = Field(h_field, w_field)

snake = Snake(0,0)
point = Entity(randint(0,w_field), randint(0, h_field))
field.entities.append(snake)
field.entities.append(point)

clear_screen()

#ciclo di gioco
draw = "si"
while True:
    if draw == "si":
        field.draw_field()
    draw = "no"

    #controllo input da tastiera + controllo bordi
    if keyboard.is_pressed("w"):
        if snake.y == 0:
            print("sei morto")
            quit()
        draw = "si"
        snake.move("w")
        while keyboard.is_pressed("w"):
            continue
        clear_screen()
    elif keyboard.is_pressed("s"):
        if snake.y == field.h - 1:
            print("sei morto")
            quit()
        draw = "si"
        snake.move("s")
        while keyboard.is_pressed("s"):
            continue
        clear_screen()
    elif keyboard.is_pressed("d"):
        if snake.x == field.w - 1:
            print("sei morto")
            quit()
        draw = "si"
        snake.move("d")
        while keyboard.is_pressed("d"):
            continue
        clear_screen()
    elif keyboard.is_pressed("a"):
        if snake.x == 0:
            print("sei morto")
            quit()
        draw = "si"
        snake.move("a")
        while keyboard.is_pressed("a"):
            continue
        clear_screen()
    elif keyboard.is_pressed("0"):
        quit()