from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_body()
        self.head = self.snake_body[0]
        self.tail = self.snake_body[len(self.snake_body) - 1]

    def create_body(self):
        for position in STARTING_POSITIONS:
            self.add_tail(position)

    def add_tail(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.shapesize(stretch_wid=0.5, stretch_len=0.5)
        snake.penup()
        snake.goto(position)
        self.snake_body.append(snake)

    def extend_tail(self):
        curr_x = self.tail.xcor()
        curr_y = self.tail.ycor()
        coordinates = (curr_x, curr_y)
        self.add_tail(coordinates)

    def move(self):
        for snake in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[snake - 1].xcor()
            new_y = self.snake_body[snake - 1].ycor()
            self.snake_body[snake].goto(new_x, new_y)
        self.head.forward(20)

    def reset(self):
        for snake in self.snake_body:
            snake.goto(1000, 1000)
        self.snake_body.clear()
        self.create_body()
        self.head = self.snake_body[0]

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


