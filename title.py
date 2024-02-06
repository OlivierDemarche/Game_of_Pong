from turtle import Turtle

TITLE_POSITION = (0, 460)
ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")


class Title(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(TITLE_POSITION)
        self.write("Welcome To The Game of Pong", align=ALIGNMENT, font=FONT)
