from turtle import Turtle

POSITION1 = (0, -400)
POSITION2 = (0, 400)


class PongNet(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.hideturtle()
        self.speed("fastest")
        self.draw_net()

    def draw_net(self):
        self.penup()
        self.goto(POSITION1)
        self.setheading(90)
        for _ in range(20):
            self.pendown()
            self.pensize(4)
            self.forward(20)
            self.penup()
            self.forward(20)
