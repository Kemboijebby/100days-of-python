from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score=0
        self.l_score=0

    def update_scoreboard(self):
            self.clear()
            self.goto(-180,200)
            self.write(self.l_score,align="center", font=("courier",80,"normal"))
            self.goto(180,200)
            self.write(self.r_score, align="center", font=("courier", 80, "normal"))


    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.l_score += 1
        self.update_scoreboard()