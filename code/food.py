from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")
        ran_x = random.randrange(-280, 280, 20)
        ran_y = random.randrange(-280, 280, 20)
        self.goto(ran_x, ran_y)
        self.refresh()

    def refresh(self):
        ran_x = random.randrange(-280, 280, 20)
        ran_y = random.randrange(-280, 280, 20)
        self.goto(ran_x, ran_y)