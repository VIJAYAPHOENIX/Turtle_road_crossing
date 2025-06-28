from turtle import Turtle
starting_position = (0,-280)
move_distance = 10
finish_line = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.starting_point()

    def starting_point(self):
        self.goto(starting_position)
        self.setheading(90)

    def move(self):
        self.forward(move_distance)

    def ending_point(self):
        if self.ycor() == finish_line:
           return  True
        else:
            return False

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!",align="center",font=("arial",24,"normal"))


