from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

screen = Screen()
screen.setup(width=1200, height=800)
screen.bgcolor("#FFE4B5")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_over = True
while game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend_snake()
        score.increase_score()

    if snake.head.xcor() > 600 or snake.head.xcor() < - 600 or snake.head.ycor() > 400 or snake.head.ycor() < - 400:
        game_over = False
        score.game_over()

    for body in snake.segments:
        if body == snake.head:
            pass
        elif snake.head.distance(body) < 5:
            game_over = False
            score.game_over()


screen.exitonclick()
