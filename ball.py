from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_paddle(self):
        self.x_move *= -1

    def bounce_wall(self):
        self.y_move *= -1

    def reset_position(self, losing_player):
        if losing_player == 'right':
            self.x_move = -10
            self.y_move = 10 * random.choice([-1, 1])
        if losing_player == 'left':
            self.x_move = 10
            self.y_move = 10 * random.choice([-1, 1])
        self.goto(0, 0)


