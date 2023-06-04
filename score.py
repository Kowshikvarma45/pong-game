
from turtle import Turtle
class Score(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x, y)
        self.r_score = 0
        self.l_score = 0
        self.write(self.r_score, align='center', font=("courier", 80, 'normal'))
        self.write(self.l_score, align='center', font=("courier", 80, 'normal'))

    def r_write(self):
        self.clear()
        self.r_score += 1
        self.write(self.r_score, align='center', font=("courier", 80, 'normal'))

    def l_write(self):
        self.clear()
        self.l_score += 1
        self.write(self.l_score, align='center', font=("courier", 80, 'normal'))
    def wins(self, l):
        self.home()
        self.write(f'PLAYER {l} wins!!', align='center', font=("courier", 60, 'normal'))

    def middle_line(self, x, y):
        self.clear()
        self.color("white")
        self.setheading(270)
        self.goto(x, y)
        while self.ycor() > -390:
            self.pendown()
            self.fd(10)
            self.penup()
            self.fd(10)