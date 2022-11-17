from random import randint
from turtle import *

rick = Turtle()

corners = int(input('How many corners do you want the shape to have?\n>>> '))

while corners < 3:
    circles = int(input('You must have at least 3 corners.S\n>>> '))

deg = 360 / corners

for i in range(corners):
    rick.forward(200 / (corners / 5))
    rick.right(deg)

done()
