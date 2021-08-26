import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # to enable control screen update instead of auto

home_position = [(0, 0), (-20, 0), (-40, 0)]
snake_squares = []

for position in home_position:
    new_sq = Turtle("square")
    new_sq.color("white")
    new_sq.penup()
    new_sq.goto(position)
    snake_squares.append(new_sq)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for sq_num in range(len(snake_squares) - 1, 0, -1):
        new_x = snake_squares[sq_num - 1].xcor()
        new_y = snake_squares[sq_num - 1].ycor()
        snake_squares[sq_num].goto(new_x, new_y)  # last square will go to second last square of snake body
    snake_squares[0].forward(20)

screen.exitonclick()
