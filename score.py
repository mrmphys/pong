from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("courier", 80, "normal"))

    def add_left_score(self):
        self.left_score += 1

    def add_right_score(self):
        self.right_score += 1
