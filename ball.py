"""Module creating the ball"""

from turtle import Turtle


class Ball(Turtle):
    """Class representing a ball object"""

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        """Method to move the ball"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Method to reverse the ball's vertical movement"""
        self.y_move *= -1

    def bounce_x(self):
        """Method to reverse the ball's horizontal movement"""
        self.x_move *= -1
