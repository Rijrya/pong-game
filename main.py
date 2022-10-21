from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

mode_select = screen.textinput("Select Mode", "What mode would you like? Easy/Medium/Hard")
speed = 0
if mode_select.lower() == 'easy':
    speed = 0.1
elif mode_select.lower() == 'medium':
    speed = 0.07
elif mode_select.lower() == 'hard':
    speed = 0.04


screen.tracer(0)

left_paddle = Paddle("left")
right_paddle = Paddle("right")
ball = Ball()
scoreboard = Scoreboard()
n = time.time()

screen.listen()
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(speed)
    ball.move()
    current_time = time.time()

    if scoreboard.over:
        game_is_on = False
        break

    if current_time - n < 1:
        pass
    else:
        if right_paddle.distance(ball) < 40:
            ball.bounce_paddle()
            n = time.time()
        if left_paddle.distance(ball) < 40:
            ball.bounce_paddle()
            n = time.time()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_wall()

    if ball.xcor() > 300:
        ball.reset_position('right')
        scoreboard.increase_score1()

    if ball.xcor() < -300:
        ball.reset_position('left')
        scoreboard.increase_score2()






screen.exitonclick()