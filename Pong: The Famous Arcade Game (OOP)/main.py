from turtle import Screen
from pong import Pong
from paddle import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

pong = Pong()
user = Paddle((350, 0))
user2 = Paddle((-350, 0))
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(user.up, "Up")
screen.onkeypress(user.down, "Down")
screen.onkeypress(user2.up, "w")
screen.onkeypress(user2.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(pong.move_speed)
    screen.update()

    pong.move()

    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.wall_bounce()

    if pong.distance(user) < 30 or pong.distance(user2) < 30:
        pong.paddle_bounce()

    if pong.xcor() > 380:
        pong.reset_position()
        scoreboard.add_l_score()

    if pong.xcor() < -380:
        pong.reset_position()
        scoreboard.add_r_score()


















screen.exitonclick()