import time
from turtle import Screen
from frame import Frame
from pongnet import PongNet
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from title import Title

STARTING_POSITION_R = (650, 0)
STARTING_POSITION_L = (-650, 0)
TIME_BETWEEN_POINT = 3


# New Point
def new_point():
    paddle_r.new_point(starting_position=STARTING_POSITION_R)
    paddle_l.new_point(starting_position=STARTING_POSITION_L)
    ball.rapidity = rapidity
    time.sleep(TIME_BETWEEN_POINT)
    ball.random_start()


# Create the main screen
screen = Screen()
screen.title("Game of Pong")
screen.setup(height=1200, width=1700)
screen.bgcolor("black")
screen.tracer(0)

# Create the frame of the game
frame = Frame()

# Create the net
pong_net = PongNet()

# Create 2 paddle
paddle_r = Paddle(starting_position=STARTING_POSITION_R)
paddle_l = Paddle(starting_position=STARTING_POSITION_L)

# Create the ball
ball = Ball()

# Add a score to reach
reach_score = int(screen.textinput("Score to reach for Win", "Put a score to reach like '10', '15',... "))

# Add a ball rapidity
rapidity = int(screen.textinput("Difficulty", "Insert a speed for the ball. from '3' to '6'"), )
ball.rapidity = rapidity
# Create the 2 ScoreBoard
score_r = ScoreBoard(side="right")
score_l = ScoreBoard(side="left")

# Create the title
title = Title()

# Create Condition for HITBOX


# Key recuperation
screen.listen()
screen.onkey(fun=paddle_r.move_up, key="Up")
screen.onkey(fun=paddle_l.move_up, key="s")
screen.onkey(fun=paddle_r.move_down, key="Down")
screen.onkey(fun=paddle_l.move_down, key="w")

# Game
game_is_on = True
ball.random_start()
while game_is_on:
    screen.update()
    ball.move()
    distance_y_r = abs(ball.ycor() - paddle_r.ycor())
    distance_y_l = abs(ball.ycor() - paddle_l.ycor())
    hitbox_face = 625 <= ball.xcor() < 635 and distance_y_r < 65 or -635 < ball.xcor() <= -625 and distance_y_l < 65
    hitbox_coin = 625 <= ball.xcor() < 630 and 65 <= distance_y_r < 70 or 625 <= ball.xcor() < 630 and 70 < distance_y_r <= 65 or -630 < ball.xcor() <= -625 and 65 <= distance_y_l < 70 or -630 < ball.xcor() <= -625 and 70 < distance_y_l <= 65
    hitbox_top_bottom = 630 <= ball.xcor() < 670 and 65 <= distance_y_r < 70 or 630 <= ball.xcor() < 670 and 70 < distance_y_r <= 65 or -670 < ball.xcor() <= -629 and 65 <= distance_y_l < 70 or -670 < ball.xcor() <= -629 and 70 < distance_y_l <= 65
    if ball.ycor() > 435 or ball.ycor() < -435:
        ball.bounce_change_direction()
    elif hitbox_face:
        ball.rapidity += 0.2
        print(ball.rapidity)
        ball.paddle_change_direction()
    elif hitbox_top_bottom:
        ball.bounce_change_direction()
    elif hitbox_coin:
        ball.other_bounce_change()
    elif ball.xcor() > 700:
        score_l.increase_score()
        new_point()
    elif ball.xcor() < -700:
        score_r.increase_score()
        new_point()
    if score_l.score == reach_score:
        pong_net.clear()
        score_l.end_game("left")
        game_is_on = False
    elif score_r.score == reach_score:
        pong_net.clear()
        score_r.end_game("right")
        game_is_on = False

screen.exitonclick()
