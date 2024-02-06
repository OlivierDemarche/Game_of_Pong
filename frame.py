from turtle import Turtle

POSITION1 = (-700, -450)
POSITION2 = (700, -450)
POSITION3 = (700, 450)
POSITION4 = (-700, 450)


class Frame(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.create_frame()

    def create_frame(self):
        self.pensize(4)
        self.goto(POSITION1)
        self.pendown()
        self.goto(POSITION2)
        self.goto(POSITION3)
        self.goto(POSITION4)
        self.goto(POSITION1)
