import time
from turtle import Turtle, Screen
import snake
import food
import score

turtle = Turtle()
screen = Screen()


def game_setup():
    screen.setup(500, 500)
    screen.title("Snake by Ninjobik")
    turtle.hideturtle()
    screen.bgcolor("black")


screen.tracer(0)

game_setup()
snake = snake.Snake(5)

screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")
screen.onkeypress(snake.grow, "q")
screen.listen()


def eat():
    if snake.head.distance(food_item.position) < 15:
        food_item.set_new_pos()
        points.add_point()
        snake.grow()


def valid_pos():
    for i in snake.snake_body[1:]:
        if snake.head.distance(i) < 19:
            return False
    if 245 > snake.head.xcor() > -245 and 245 > snake.head.ycor() > -245:
        return True
    else:
        return False


food_item = food.Food()
points = score.Score()

game_on = True
while game_on:
    eat()
    screen.update()
    time.sleep(0.1)
    snake.move()
    if not valid_pos():
        snake.restart_snake()
        points.restart_game()


screen.exitonclick()
