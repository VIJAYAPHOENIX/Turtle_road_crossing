from turtle import Turtle
import  random

COLORS = ["orange","red","black","yellow","green","pink","blue"]
MOVEMENT_PACE = 10
INCREASE_PACE = 5

class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVEMENT_PACE
        self.create_cars()

    def create_cars(self):
        chance = random.randint(1,5)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += INCREASE_PACE
