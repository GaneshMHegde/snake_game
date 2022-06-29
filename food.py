from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.speed(0)
        self.color('blue')
        self.resizemode('user')
        self.shapesize(stretch_wid=0.25,stretch_len=0.25,outline=0.25)
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)

