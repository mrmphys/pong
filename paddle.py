from turtle import Turtle

DEFAULT_PADDLE_WIDTH = 1
DEFAULT_PADDLE_LEN = 5

class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        self.x = x_cor
        self.y = y_cor
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=DEFAULT_PADDLE_WIDTH, stretch_len=DEFAULT_PADDLE_LEN)
        self.penup()
        self.setheading(90)
        self.goto(x=self.x, y=self.y)
        self.color("white")

    def move_up(self):
        self.forward(40)

    def move_down(self):
        self.backward(40)
