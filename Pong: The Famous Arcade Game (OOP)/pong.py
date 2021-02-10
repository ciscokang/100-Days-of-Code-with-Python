from turtle import Turtle
from random import randint, choice


class Pong(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # def starting_angle(self):
    #     angle_1 = randint(0, 45)
    #     angle_2 = randint(315, 359)
    #     angle_3 = randint(180, 225)
    #     angle_4 = randint(135, 179)
    #     angles = [angle_1, angle_2, angle_3, angle_4]
    #     random_angle = choice(angles)
    #     self.setheading(random_angle)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.paddle_bounce()
        self.move_speed = 0.1

