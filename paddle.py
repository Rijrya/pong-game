from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        if position == "left":
            self.goto(-287, 0)
        elif position == "right":
            self.goto(280, 0)

    def up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)