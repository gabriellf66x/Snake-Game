import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

game_is_on = True

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 35:
        score.track_score()
        food.refresh()
        snake.tail()

    for _ in range(1, len(snake.squares)):
        if snake.head.distance(snake.squares[_]) < 2:
            game_is_on = False

    if snake.head.xcor() == 280 or snake.head.xcor() == -280 or snake.head.ycor() == 280 or snake.head.ycor() == -280:
        game_is_on = False

score.game_over()
screen.exitonclick()
