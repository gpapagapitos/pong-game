"""Module creating the ball"""

from turtle import Turtle


class Ball(Turtle):
    """Class representing a ball object"""

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()

    def move(self):
        """Method to move the ball"""
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)