"""Module creating scoreboard and tracking the score"""

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Method to update the scoreboard"""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        """Method to increase left player's score by 1 and update scoreboard"""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Method to increase right player's score by 1 and update scoreboard"""
        self.r_score += 1
        self.update_scoreboard()
