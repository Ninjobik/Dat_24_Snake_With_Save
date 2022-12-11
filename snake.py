from turtle import Turtle
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    def __init__(self, length):
        self.snake_body = []
        self.snake_length = length
        self.create_snake(self.snake_length)
        self.head = self.snake_body[0]

    def create_snake(self, length):
        for i in range(length):
            square = self.add_square()
            square.setposition(i * -20, 0)
            self.snake_body.append(square)

    def add_square(self):
        new_square = Turtle("square")
        new_square.shapesize(0.9, 0.9)
        new_square.penup()
        new_square.color("white")
        return new_square

    def move(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[i].setposition(self.snake_body[i - 1].pos())
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def grow(self):
        new_s = self.add_square()
        new_s.setposition(self.head.position())
        self.snake_body.append(new_s)

    def restart_snake(self):
        for each in self.snake_body:
            each.setposition(1000, 1000)
        self.snake_body.clear()
        self.create_snake(self.snake_length)
        self.head = self.snake_body[0]


