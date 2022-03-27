import turtle as tt
import time
from snake_game import Snake
from food import Food
from scoreboard import Scoreboard

tt.colormode(255)

screen = tt.Screen()

# Snake Game

screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game") 
screen.tracer(0) # Turns the turtle animation off, basically turns the turtles off

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update() # update the screen as changes happen
    time.sleep(0.1)
    snake.move()

    # Detect collison with food
    if snake.head.distance(food) < 15:
        snake.extend_snake()
        food.move()
        score.increment()

    # Detect Wall Collison
    top = snake.head.ycor() > 295
    bottom = snake.head.ycor() < -295
    left = snake.head.xcor() < -295
    right = snake.head.xcor() > 295

    if top or bottom or left or right:
        game_on = False
        score.game_over()

    # Detect collision with itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()
        




screen.exitonclick()