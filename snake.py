from turtle import Screen, Turtle
STARTING_POSITION = [(-20,0),(-40,0),(-60,0)] #CONSTANT
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segment_list=[] # attribute
        # method to create snake. Each time when we are creating the snake object, a snake will be created
        # that's why this method is under init
        self.creat_snake()

    def creat_snake(self):
        for position in STARTING_POSITION:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segment_list.append(segment) #need to refer the attribute segment_list.hence need self eky word

    #method to move the snake
    def move(self):
          for seg_num in range(len(self.segment_list) - 1, 0, -1):
            new_x = self.segment_list[seg_num - 1].xcor()  # new x cordinates of segment
            new_y = self.segment_list[seg_num - 1].ycor()  # new y cordinates of segment
            self.segment_list[seg_num].goto(new_x, new_y)  # assign the cordinate
          self.segment_list[0].forward(MOVE_DISTANCE)
