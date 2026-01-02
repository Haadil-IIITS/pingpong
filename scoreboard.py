from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.player1=0
        self.player2=0



    def writing(self):
        self.clear()
        self.goto(-350.00, 230.00)
        self.write(f"{self.player1}", False, 'left', font=("Sans-Serif", 26, "normal"))
        self.goto(350.00, 230.00)
        self.write(f"{self.player2}", False, 'right', font=("Sans-Serif", 26, "normal"))

    def final(self):
        if self.player1>self.player2:
            self.goto(0,0)
            self.write("Winner is player 1", False, 'center', font=("Sans-Serif", 14, "normal"))

            self.goto(0,-20)
            self.write("Game Over", False, 'center', font=("Sans-Serif", 14, "normal"))


        else:
            self.goto(0, 0)
            self.write("Winner is player 2", False, 'center', font=("Sans-Serif", 14, "normal"))

            self.goto(0, -20)
            self.write("Game Over", False, 'center', font=("Sans-Serif", 14, "normal"))



