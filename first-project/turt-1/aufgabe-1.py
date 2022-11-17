from random import randint
from turtle import *

rick = Turtle()

circles = int(input('How many circles do you want?\n>>> '))
while circles > 100:
    circles = int(input('Too many circles, please input a lower amount\n>>> '))
rick.penup()

for i in range(circles):
    pos1 = randint(-400, 400)
    pos2 = randint(-400, 400)
    size = randint(5, 100)

    rick.goto(pos1, pos2)
    rick.pendown()
    rick.circle(size)
    rick.penup()
done()