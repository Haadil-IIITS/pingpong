from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.setheading(90)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=3)
        self.speed("fastest")

    def front(self):
        if self.ycor()>250:
            pass
        else:
            self.setheading(90)
            self.forward(30)

    def back(self):
        if self.ycor() <-250:
            pass
        else:
            self.setheading(-90)
            self.forward(30)
