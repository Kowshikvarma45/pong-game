
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1, outline=3)
        self.goto(x, y)
    def move_up(self):
        if self.xcor() < 0:
            y = self.ycor()
            y += 20
            self.goto(-487, y)
        else:
            y = self.ycor()
            y += 20
            self.goto(480, y)

    def move_down(self):
        if self.xcor() < 0:
            y = self.ycor()
            y -= 20
            self.goto(-487, y)
        else:
            y = self.ycor()
            y -= 20
            self.goto(480, y)

