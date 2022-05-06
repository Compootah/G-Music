from math import *
from turtle import *
from turtle import Screen, Turtle
import turtle
from time import *

#Window Setup
wn = turtle.Screen()
wn.title("Ear Training and Music Theory")
wn.setup(width = 1000, height = 1000)
wn.tracer(0)

#Functions
dot = Turtle()

def draw_onclick(x, y):
    dot.dot(100, "cyan")
    

#Starting Screen

#Box 1 is the very first box. (Top Left)
box_1 = turtle.Turtle()
box_1.shape("square")
box_1.shapesize(stretch_len = 20, stretch_wid = 20)
box_1.color("white")
box_1.penup()
box_1.goto(-250, 250)

box_1_contents = turtle.Turtle()
box_1_contents.shape("square")
box_1_contents.fillcolor(0.25, 0.620, 0.99999999)
box_1_contents.penup()
box_1_contents.goto(-250, 250)
box_1_contents.shapesize(stretch_len = 19.5, stretch_wid = 19.5)
box_1_contents.color(0.25, 0.620, 0.99999999)
box_1_contents.onclick(draw_onclick)
dot.hideturtle()

#Background Colour
COLOR = (0, 0.4, 0.9999999)  # (R, G, B)
TARGET = (0.69, 0, 0.420)  # (R, G, B)

screen = Screen()
screen.tracer(False)

WIDTH, HEIGHT = screen.window_width(), screen.window_height()

deltas = [(hue - COLOR[index]) / HEIGHT for index, hue in enumerate(TARGET)]

turtle = Turtle()
turtle.color(COLOR)

turtle.penup()
turtle.goto(-WIDTH/2, HEIGHT/2)
turtle.pendown()

direction = 1

for distance, y in enumerate(range(HEIGHT//2, -HEIGHT//2, -1)):

    turtle.forward(WIDTH * direction)
    turtle.color([COLOR[i] + delta * distance for i, delta in enumerate(deltas)])
    turtle.sety(y)

    direction *= -1

screen.tracer(True)
screen.mainloop()

#Main Loop
while True:
    screen.update()
    wn.update()
    