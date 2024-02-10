from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width =600, height =600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) #off the screen

snake = Snake()
food = Food()
scoreboard = Scoreboard()

#Key binding
screen.listen()
screen.onkey(snake.up,"Up") #calling the up method in onkey method of screen
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_is_on = True
while game_is_on:
    screen.update()  # Update the screen after moving the all the positions of the segments
    time.sleep(0.1)  # delay screen update by 1 sec
    snake.move()

    #Detect the food and create the food in random location
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

     #Detect the collision to walls
    if snake.head.xcor()> 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect Collision with snake's tail
    for segment in snake.segment_list:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment)<10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()