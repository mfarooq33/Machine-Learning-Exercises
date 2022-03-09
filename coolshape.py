
from turtle import *
import tkinter
bgcolor('black')
hideturtle()
for i in range(120):
    color('blue')
    circle(i)
    color('white')
    circle(i*0.8)
    color('green')
    circle(i*0.9)
    right(3)
    forward(3)
done()    