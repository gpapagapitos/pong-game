"""Pong game"""
# pylint: disable=C0103
from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

paddle = Paddle()

screen.exitonclick()
