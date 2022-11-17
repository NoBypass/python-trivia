from random import randint
from turtle import *

rick = Turtle()

rick.penup()
rick.goto(0, 0)
rick.pendown()
rick.begin_fill()
rick.color('#FEFF00')
for i in range(1, 5):
    rick.forward(100)
    rick.right(90)
rick.end_fill()
rick.begin_fill()
rick.color('#FF0000')
rick.goto(50, 50)
rick.goto(100, 0)
rick.goto(0, 0)
rick.end_fill()
rick.penup()
rick.goto(90, -10)
rick.pendown()
rick.begin_fill()
rick.color('#003EFF')
for i in range(1, 5):
    rick.right(90)
    rick.forward(30)
rick.end_fill()
rick.penup()
rick.goto(10, -30)
rick.pendown()
rick.begin_fill()
rick.color('#828282')
for i in range(1, 3):
    rick.forward(30)
    rick.right(90)
    rick.forward(70)
    rick.right(90)
rick.end_fill()

done()
