from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(coordinates)

    def up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

    def player1(self):
        self.goto(-280, -350)
        self.write("Player 1",align="center",font=("Ariel",22,'bold'))

    def player2(self):
        self.goto(280, 350)
        self.write("Player 2",align="center",font=("Ariel",22,'bold'))