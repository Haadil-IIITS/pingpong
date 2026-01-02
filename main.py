from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
scoreboard=Scoreboard()
from scoreboard import Scoreboard
#create the screen
screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("PingPong Game")
screen.tracer(0)

r_paddle=Paddle((350.00,0.00))
l_paddle=Paddle((-350.00,0.00))

screen.listen()
screen.onkey(key="Up",fun=r_paddle.front)
screen.onkey(key="Down",fun=r_paddle.back)
screen.onkey(key="w",fun=l_paddle.front)
screen.onkey(key="s",fun=l_paddle.back)
game_is =True


ball=Ball()
scoreboard.writing()
while game_is:
    screen.update()
    time.sleep(0.1)
    if r_paddle.distance(ball)<25:
        ball.j=-1
    elif l_paddle.distance(ball)<25:
        ball.j=1
    ball.move()

    if ball.xcor() > 380:
        scoreboard.player1 += 1
        ball.goto(0, 0)
        scoreboard.writing()

    if ball.xcor() < -380:
        scoreboard.player2 += 1
        ball.goto(0, 0)
        scoreboard.writing()

    if scoreboard.player1==3 or scoreboard.player2 == 3 :
        scoreboard.final()
        game_is =False



screen.exitonclick()
