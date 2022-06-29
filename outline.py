from turtle import Turtle

class Outline(Turtle):
    def __init__(self):
        super().__init__()
        self.color('yellow')
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.goto(290, 290)
        self.pendown()
        self.right(90)
        self.forward(580)
        self.right(90)
        self.forward(580)
        self.right(90)
        self.forward(580)
        self.right(90)
        self.forward(580)
        self.penup()
