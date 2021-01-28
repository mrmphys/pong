from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.y_move = 10
        self.x_move = 10
        self.speeding = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y_direction(self):
        self.y_move *= -1
        self.speeding *= 0.9

    def bounce_x_direction(self):
        self.x_move *= -1
        self.speeding *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.speeding = 0.1
        time.sleep(0.5)
