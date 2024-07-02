"""Module creating the paddle"""

from turtle import Turtle

MOVEMENT_AMT = 20


class Paddle(Turtle):
    """Class representing a paddle"""

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        """Method to move the paddle up"""
        new_y = self.ycor() + MOVEMENT_AMT
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Method to move the paddle down"""
        new_y = self.ycor() - MOVEMENT_AMT
        self.goto(self.xcor(), new_y)
