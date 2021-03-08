from turtle import Turtle

ALIGN = 'center'
FONT = ("Ariel", 40, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.create_left_score()
        self.create_right_score()

    def create_left_score(self):
        self.goto(-120, 245)
        self.color("red")
        self.write(f"THOR {self.score_left}", align=ALIGN, font=FONT)

    def create_right_score(self):
        self.goto(120, 245)
        self.color('blue')
        self.write(f"{self.score_right} LOKI", align=ALIGN, font=FONT)

    def increase_left_score(self):
        self.score_left += 1
        self.clear()
        self.create_left_score()

    def increase_right_score(self):
        self.score_right += 1
        self.clear()
        self.create_right_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGN, font=FONT)