from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.color("white")
        self.ht()
        self.penup()
        self.sety(260)
        self.over = False
        self.write(f"Score: {self.score1} - {self.score2}", False, align="center", font=('Courier', 20, 'normal'))

    def game_over(self, winner):
        self.sety(0)
        self.write(f"GAME OVER\n{winner} wins!", align="center", font=('Courier', 20, 'normal'))
        self.write(f"{winner} wins!", align="center", font=('Courier', 20, 'normal'))

    def increase_score2(self):
        self.clear()
        self.score2 += 1
        self.write(f"Score: {self.score1} - {self.score2}", False, align="center", font=('Courier', 20, 'normal'))
        if self.score2 >= 10:
            self.game_over("Player 2")
            self.over = True

    def increase_score1(self):
        self.clear()
        self.score1 += 1
        self.write(f"Score: {self.score1} - {self.score2}", False, align="center", font=('Courier', 20, 'normal'))
        if self.score1 >= 10:
            self.game_over("Player 1")
            self.over = True



