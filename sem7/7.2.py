from random import randrange as rnd, choice
from tkinter import *
import math
import time

root = Tk()
fr = Frame(root)
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

class Ball:

    def __init__(self, x=40, y=450):
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color)
        self.live = 30

    def set_coords(self):
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

    def move(self):
        self.vy -= 1  
        self.x += self.vx
        self.y -= self.vy
        self.set_coords()
        
        if self.x + self.r > 800 or self.x - self.r < 0:
            self.vx = -self.vx * 0.7  
        if self.y + self.r > 600:
            self.vy = -self.vy * 0.7
            self.y = 600 - self.r  

    def hittest(self, ob):
        dist = ((self.x - ob.x) ** 2 + (self.y - ob.y) ** 2) ** 0.5
        return dist <= self.r + ob.r


class Gun:
    
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 0  
        self.x = 20  
        self.y = 450
        self.id = canv.create_line(self.x, self.y, self.x + 30 * math.cos(self.an), 
                                   self.y + 30 * math.sin(self.an), width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        global balls, bullet
        bullet += 1
        new_ball = Ball()
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = -self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        if event:
            self.an = math.atan((event.y - self.y) / (event.x - self.x))
        color = 'orange' if self.f2_on else 'black'
        canv.itemconfig(self.id, fill=color)
        canv.coords(self.id, self.x, self.y, 
                    self.x + max(self.f2_power, 20) * math.cos(self.an), 
                    self.y + max(self.f2_power, 20) * math.sin(self.an))

    def power_up(self):
        if self.f2_on:
            self.f2_power = min(100, self.f2_power + 1)
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class Target:

    def __init__(self):
        self.points = 0
        self.live = 1
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(30, 30, text=self.points, font='28')
        self.new_target()  

    def new_target(self):
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(10, 50)
        color = self.color = 'red'
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)


t1 = Target()
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = Gun()
bullet = 0
balls = []


def new_game(event=''):
    global gun, t1, screen1, balls, bullet
    t1.new_target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    z = 0.03
    t1.live = 1
    while t1.live or balls:
        for b in balls:
            b.move()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    root.after(1, new_game)

new_game()
root.mainloop()
