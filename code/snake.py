from turtle import Turtle

STARTING_POSITIONS = [0, -20, -40]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        self.head.color("red")
        self.head.shape("circle")
        head_width = 20
        head_height = 40
        self.head.shapesize(head_width / 20, outline=head_height / 10)
        self.head.color("red")

    def add_segement(self):
        new = Turtle("square")
        new.color("red")
        new.penup()
        self.segment.append(new)

    def create_snake(self):

        for i in STARTING_POSITIONS:
            start = Turtle("square")
            start.color("red")
            start.penup()
            start.setx(i)
            self.segment.append(start)
    def move(self):
        for i in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[i - 1].xcor()
            new_y = self.segment[i - 1].ycor()
            self.segment[i].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):
        for i in self.segment:
            i.goto(1000,1000)

        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]
