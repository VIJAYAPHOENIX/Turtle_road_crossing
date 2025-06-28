from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-200,260)
        self.player_score = 0
        self.update()

    def update(self):
        self.clear()
        self.write(f"LEVEL : {self.player_score}",align="left",font=("courier",20,"normal"))

    def level_up(self):
        self.player_score += 1
        self.update()

