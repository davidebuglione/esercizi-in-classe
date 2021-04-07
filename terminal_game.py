import keyboard
import os
from random import randint
import time
from threading import Thread

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
        if direction == "w":
            futureY -= 1
            self.snake_drawing = "[|]"
        elif direction == "s":
            futureY += 1
            self.snake_drawing = "[|]"
        elif direction == "d":
            futureX += 1
            self.snake_drawing = "[-]"
        elif direction == "a":
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
        entity.assign_coords(entity, randint(0,w_field-1), randint(0,h_field-1))

    def assign_coords(self, entity, x, y):
        entity.x = x
        entity.y = y

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

#auto_move = "right"
class Motion_thread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.auto_move = "right"
    def run(self):
        while True:
            if keyboard.is_pressed("w"):
                self.auto_move = "up"
                while keyboard.is_pressed("w"):
                    continue
            elif keyboard.is_pressed("s"):
                self.auto_move = "down"
                while keyboard.is_pressed("s"):
                    continue
            elif keyboard.is_pressed("d"):
                self.auto_move = "right"
                while keyboard.is_pressed("d"):
                    continue
            elif keyboard.is_pressed("a"):
                self.auto_move = "left"
                while keyboard.is_pressed("a"):
                    continue
            
            if keyboard.is_pressed("0"):
                quit()        

#intro
clear_screen()
print("Today,", time.ctime(), ",you are going to accept a very difficult challenge, are you ready?")
input()

#richiesta misure campo all'utente e creazione classi
h_field = int(input("inserire l'altezza del campo"))
print()
w_field = int(input("inserire la larghezza del campo"))
field = Field(h_field, w_field)

snake = Snake(0,0)
point = Entity(randint(0,w_field-1), randint(0, h_field-1))
field.entities.append(snake)
field.entities.append(point)

motion_thread = Motion_thread()

clear_screen()

motion_thread.start()
#ciclo di gioco
while True:
    field.draw_field()

    if motion_thread.auto_move == "right":
        snake.move("d")
    elif motion_thread.auto_move == "left":
        snake.move("a")
    elif motion_thread.auto_move == "up":
        snake.move("w")
    elif motion_thread.auto_move == "down":
        snake.move("s")
    '''
    if keyboard.is_pressed("w"):
        auto_move = "up"
        while keyboard.is_pressed("w"):
            continue
    elif keyboard.is_pressed("s"):
        auto_move = "down"
        while keyboard.is_pressed("s"):
            continue
    elif keyboard.is_pressed("d"):
        auto_move = "right"
        while keyboard.is_pressed("d"):
            continue
    elif keyboard.is_pressed("a"):
        auto_move = "left"
        while keyboard.is_pressed("a"):
            continue
    
    if keyboard.is_pressed("0"):
        quit()
    '''
    if snake.y == -1 or snake.y == field.h or snake.x == field.w or snake.x == -1:
        print("sei morto")
        quit()
    time.sleep(0.5)
    clear_screen()