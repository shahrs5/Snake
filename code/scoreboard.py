from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.content = open("data.txt")
        self.highscore = self.content.read()
        self.color("white")
        self.penup()
        self.write("Hello World, Made By Shaheer")
        self.goto(0, 260)
        self.pendown()
        self.hideturtle()
        self.update()

    def reset(self):
        if self.score > int(self.highscore):
            with open("data.txt", "w") as text:
                text.write(f"{self.score}")

        self.score = 0
        self.update()

    def game_over(self):
        self.write("Game Over", False, align="center", font=("Comic Sans MS", 12, "bold"))

    def next_level(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.content = open("data.txt")
        self.highscore = self.content.read()
        self.write(f"Score : {self.score} High Score : {self.highscore}", False, align="center",
                   font=("Comic Sans MS", 12, "bold"))
