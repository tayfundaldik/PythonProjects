import turtle as t
import random
from turtle import Turtle,Screen
color_list=[(245, 243, 238), (247, 242, 244), (240, 245, 241), (202, 164, 109), (238, 240, 245), (150, 75, 49),
 (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86),
 (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50),
 (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100),
 (107, 127, 153), (174, 94, 97), (176, 192, 209)]

def dota():
    for n in range(10):
        n+=1
        tim.penup()
        tim.fd(50)
        tim.pendown()
        ry=random.choice(color_list)
        tim.dot(20,ry )
        tim.penup()
        tim.fd(50)
        tim.pendown()
        tim.position()
        (0.00,-0.00)
        tim.heading()
tim=t.Turtle()

for a in range (10):
    a+=1
    dota()




screen=Screen()
screen.exitonclick()

