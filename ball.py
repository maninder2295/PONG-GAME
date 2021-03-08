from turtle import Turtle
DIRECTION = [20,30,40,45,55,65,70,80]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def create_ball(self):
        self.shape("circle")
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color("white")
        self.penup()
        self.goto(0, 0)

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x_r(self):
        self.x_move *= -1
        self.color('red')
        self.move_speed *= 0.9

    def bounce_x_l(self):
        self.x_move *= -1
        self.color('blue')
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x_l()
        self.color("white")
        self.move_speed = 0.1

