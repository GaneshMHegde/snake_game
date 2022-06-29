from turtle import  Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,290)
        self.write(f'Score: {self.score}',False,'center',("Arial", 24, "normal"))



    def new_score(self):
        self.score+=1
        self.clear()
        self.goto(0,290)
        self.write(f'Score: {self.score}', False, 'center', ("Arial", 24, "normal"))


    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER!!', False, 'center', ("Arial", 24, "normal"))

