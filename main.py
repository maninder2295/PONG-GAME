from turtle import Turtle, Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.title("Welcome to Pong Game")
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

# Split Screen by Line
line = Turtle()
line.color('white')
line.penup()
line.goto(0, 300)
line.setheading(270)
line.pensize(3)
line.hideturtle()

while line.ycor() > -300:
    line.pendown()
    line.forward(20)
    line.penup()
    line.forward(20)

scoreboard = Scoreboard()

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

screen.listen()
screen.onkey(l_paddle.up, "a")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

ball = Ball()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_ball()
    scoreboard.create_left_score()
    scoreboard.create_right_score()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x_l()
        scoreboard.increase_right_score()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x_r()
        scoreboard.increase_left_score()


    # Detect if the ball goes out of bounds at the edge of the screen
    # Detect R paddle misses
    if ball.xcor() > 360:
        ball.reset_position()
        scoreboard.increase_left_score()

    # Detect L paddle misses
    if ball.xcor() < -360:
        ball.reset_position()
        scoreboard.increase_right_score()







screen.exitonclick()
