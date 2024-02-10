from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width =600, height =600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) #off the screen

snake = Snake()
food = Food()

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


screen.exitonclick()