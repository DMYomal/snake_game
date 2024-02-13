from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 16, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score =0
        self.highscore =0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Your Score: {self.score} High Score: {self.highscore}", move=False, align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", align = ALIGNMENT, font = FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score +=1
        # self.clear()
        self.update_scoreboard()



