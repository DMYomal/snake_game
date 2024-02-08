from turtle import Screen, Turtle

screen = Screen()
screen.setup(width =600, height =600)
screen.bgcolor("black")
screen.title("Snake Game")

starting_position = [(-20,0),(-40,0),(-60,0)]
segment_list = []

for position in starting_position:
    segment = Turtle("square")
    segment.color("white")
    segment.goto(position)
    segment_list.append(segment)



screen.exitonclick()