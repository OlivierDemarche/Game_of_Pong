from turtle import Turtle

SCORE_POSITION_R = (55, 350)
SCORE_POSITION_L = (-55, 350)
ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")


class ScoreBoard(Turtle):

    def __init__(self, side):
        super().__init__()
        self.penup()
        self.score = 0
        self.hideturtle()
        if side == "right":
            position = SCORE_POSITION_R
        elif side == "left":
            position = SCORE_POSITION_L
        self.goto(position)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def end_game(self, player):
        self.goto(0, 0)
        self.write(f"The player '{player}' has reach {self.score} and win the Game", align=ALIGNMENT, font=FONT)
