import  turtle
from snake_body  import Snake
from food import Food
from score import Score
from outline import Outline
import time

screen=turtle.Screen()
screen.screensize(canvwidth=600, canvheight=600, bg='black')
screen.title('Snake Game')

snake=Snake()
outline=Outline()
food=Food()
score = Score()
snake.create_snake()
turtle.tracer(0)
game_is_on = True
while game_is_on:
    turtle.update()
    time.sleep(0.2)
    snake.move()
    turtle.listen()
    screen.onkey(snake.turn_left,'Left')
    screen.onkey(snake.turn_right,'Right')
    screen.onkey(snake.turn_up,'Up')
    screen.onkey(snake.turn_down,'Down')

    if snake.snake_body[0].distance(food)<10:
        food.refresh()
        score.new_score()
        snake.add_segment()

    if snake.snake_body[0].xcor()>280 or snake.snake_body[0].xcor()<-280 or snake.snake_body[0].ycor()>280 or snake.snake_body[0].ycor()<-280:
        game_is_on=False
        score.game_over()

    if game_is_on==True:
        game_is_on=snake.collistion()
        if game_is_on==False:
            score.game_over()

screen.exitonclick()