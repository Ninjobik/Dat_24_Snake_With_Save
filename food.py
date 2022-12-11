import random
from turtle import Turtle


class Food:
    def __init__(self):
        self.position = None
        self.food = Turtle("square")
        self.food.penup()
        self.food.color("green")
        self.food.shapesize(0.9, 0.9)
        self.set_new_pos()

    def set_pos(self):
        xPos = random.randint(-12, 12) * 20
        yPos = random.randint(-12, 12) * 20
        return xPos, yPos

    def set_new_pos(self):
        self.position = self.set_pos()
        self.food.setposition(self.position)
