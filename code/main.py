import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

def end_game():
    screen.bye()


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")

screen.onkey(end_game, "space")  # To quit the game


game_on = True
while game_on:
    snake.move()
    screen.update()
    time.sleep(0.1)

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_segement()
        scoreboard.next_level()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset()
        scoreboard.reset()

    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            scoreboard.reset()

screen.exitonclick()
