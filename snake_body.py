import  turtle

class Snake:
    def __init__(self):
        self.snake_body = []


    def create_snake(self):
        a = 0
        turtle.resizemode('user')
        for i in range(3):
            snake = turtle.Turtle()
            snake.penup()
            snake.shapesize(stretch_wid=0.5, stretch_len=0.5, outline=0.5)
            snake.shape('square')
            snake.color('white')
            snake.forward(-a)
            self.snake_body.append(snake)
            a += 10

    def move(self):
        for body in range(len(self.snake_body) - 1, 0, -1):
            x = self.snake_body[body - 1].xcor()
            y = self.snake_body[body - 1].ycor()
            self.snake_body[body].goto(x, y)
        self.snake_body[0].forward(10)

    def add_segment(self):
       last_snake=self.snake_body[-1]
       x = last_snake.xcor()
       y = last_snake.ycor()
       direction=self.snake_body[-1].heading()
       snake = turtle.Turtle()
       snake.shape('square')
       snake.color('white')
       snake.penup()
       snake.shapesize(stretch_wid=0.5, stretch_len=0.5, outline=0.5)
       self.snake_body.append(snake)
       self.snake_body[-1].setheading(direction)
       if direction==0 or direction==180:
           a=-10
           b=0
       else:
           a=0
           b=-10
       self.snake_body[-1].goto(x-a,y-b)

    def collistion(self):
        for segment in self.snake_body:
            if segment==self.snake_body[0]:
                pass
            elif segment==self.snake_body[1]:
                pass
            elif self.snake_body[0].distance(segment)<5:
                return False
        return True



    turtle.mode('standard')
    def turn_left(self):
        if self.snake_body[0].heading()!=0:
            self.snake_body[0].setheading(180)

    def turn_right(self):
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)


    def turn_up(self):
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90)

    def turn_down(self):
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)
