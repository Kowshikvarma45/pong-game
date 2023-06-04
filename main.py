from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

my_Screen = Screen()
my_Screen.setup(width=1000, height=700)
my_Screen.bgcolor("black")
my_Screen.tracer(0)
l_paddle = Paddle(-487, 0)
r_paddle = Paddle(480, 0)
m_line = Score(0, 260)
m_line.middle_line(0, 390)
ball = Ball()
l_score = Score(-100, 250)
r_score = Score(100, 250)
my_Screen.listen()
my_Screen.onkeypress(r_paddle.move_up, "Up")
my_Screen.onkeypress(r_paddle.move_down, "Down")
my_Screen.onkeypress(l_paddle.move_up, "w")
my_Screen.onkeypress(l_paddle.move_down, "s")
game_on = True


while game_on:
    my_Screen.update()
    ball.move()
    if ball.ycor() >= 340 or ball.ycor() <= -340:
        ball.bounce()
    if (ball.xcor() > 460 and ball.distance(r_paddle) < 50) or (ball.xcor() < -460 and ball.distance(l_paddle) < 50):
        ball.xbounce()
    if ball.xcor() > 480:
        l_score.l_write()
        ball.set()
    if ball.xcor() < -495:
        r_score.r_write()
        ball.set()

    time.sleep(ball.time)
    if l_score.l_score == 10:
      game_on = False
      l_score.wins("left")
    if r_score.r_score == 10:
      game_on = False
      r_score.wins("right")



my_Screen.exitonclick()
