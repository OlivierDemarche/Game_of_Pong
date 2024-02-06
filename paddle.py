from turtle import Turtle

SPEED = 25


class Paddle(Turtle):

    def __init__(self, starting_position):
        super().__init__()
        self.segments = []
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.new_point(starting_position)

    def move_up(self):
        new_y = self.ycor() + SPEED
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - SPEED
        self.goto(self.xcor(), new_y)

    def new_point(self, starting_position):
        self.goto(starting_position)
