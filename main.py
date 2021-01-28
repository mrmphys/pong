from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

score = Score()
score.update_score()
screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

paddle_left = Paddle(-450, 0)
paddle_right = Paddle(450, 0)

ball = Ball()

screen.listen()
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")

play_mode = True
time.sleep(3)
while play_mode:
    time.sleep(ball.speeding)
    screen.update()
    ball.move()

    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y_direction()

    if (ball.distance(paddle_right) < 50 and ball.xcor() > 430) or (ball.distance(paddle_left) < 50 and ball.xcor() < -430):
        ball.bounce_x_direction()

    if ball.xcor() < -490:
        ball.reset()
        score.add_right_score()
        score.update_score()

    if ball.xcor() > 490:
        ball.reset()
        score.add_left_score()
        score.update_score()


   # play_mode = False


screen.exitonclick()
