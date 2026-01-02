from turtle import Turtle,Screen

from scoreboard import Scoreboard
scoreboard=Scoreboard()
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize()
        self.speed(1)
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.penup()
        self.goto(0.00,0.00)
        self.i=1
        self.j=1

    def move(self):
        new_x=self.xcor()+10*self.j
        new_y=self.ycor()+10*self.i
        if new_y>=290:
            self.i=-1
        elif new_y <=-290:
            self.i=1













        self.goto(new_x,new_y)

