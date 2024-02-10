from turtle import Turtle
STARTING_POSITION = [(-20,0),(-40,0),(-60,0)] #CONSTANT
MOVE_DISTANCE = 20
#Snake should not be able to turn into the opposite side while moving
UP = 90
DOWN = 270
RIGHT = 0
LEFT =180

class Snake:
    def __init__(self):
        self.segment_list=[] # attribute
        # method to create snake. Each time when we are creating the snake object, a snake will be created by calling the function
        # that's why this method is under init
        self.creat_snake()
        self.head =self.segment_list[0]

    def creat_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segment_list.append(segment)  # need to refer the attribute segment_list.hence need self Key word

    def extend(self):
    # add a new segment to the snake's tial(last segment position)
        self.add_segment(self.segment_list[-1].position())

    #method to move the snake
    def move(self):
          for seg_num in range(len(self.segment_list) - 1, 0, -1):
            new_x = self.segment_list[seg_num - 1].xcor()  # new x cordinates of segment
            new_y = self.segment_list[seg_num - 1].ycor()  # new y cordinates of segment
            self.segment_list[seg_num].goto(new_x, new_y)  # assign the cordinate
          self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)