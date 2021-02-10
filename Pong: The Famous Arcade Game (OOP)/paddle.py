from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        x, y = self.position()
        if y < 260:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)
        elif y > 260:
            self.undo()

    def down(self):
        x, y = self.position()
        if y > -260:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
        elif y < -260:
            self.undo()









