from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width =600, height =600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) #off the screen

snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()  # Update the screen after moving the all the positions of the segments
    time.sleep(0.1)  # delay screen update by 1 sec
    snake.move()




screen.exitonclick()