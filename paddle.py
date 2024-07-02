"""Module creating the paddle"""

from turtle import Turtle


class Paddle(Turtle):
    """Class representing a paddle"""
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
