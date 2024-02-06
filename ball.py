from turtle import Turtle
import random

LAUNCH_ANGLE = 60


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.width(10)
        self.shapesize(1.5)
        self.penup()
        self.rapidity = 0

    def random_start(self):
        self.goto(0, 0)
        random_right = list(range(0 - LAUNCH_ANGLE, LAUNCH_ANGLE, 1))
        random_left = list(range(180 - LAUNCH_ANGLE, 180 + LAUNCH_ANGLE, 1))
        random_angle = random_right + random_left
        self.setheading(random.choice(random_angle))

    def move(self):
        self.forward(self.rapidity)

    def bounce_change_direction(self):
        heading_value = self.heading()
        new_heading_value = 360 - heading_value
        self.setheading(new_heading_value)

    def paddle_change_direction(self):
        heading_value = self.heading()
        new_heading_value = 180 - heading_value
        print(new_heading_value)
        self.setheading(new_heading_value)

    def other_bounce_change(self):
        heading_value = self.heading()
        new_heading_value = (heading_value - 180) + random.randint(-10,10)
        self.setheading(new_heading_value)
        self.rapidity += 2
