import random

import colorgram
import turtle as t

colors = colorgram.extract('image.jpg', 42)
rgb_colors = []
for c in colors:
    color = (c.rgb.r, c.rgb.g, c.rgb.b)
    rgb_colors.append(color)

t.colormode(255)

tim = t.Turtle()
tim.speed("fastest")
tim.width(20)
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
for i in range(1, 101):
    tim.dot(30, random.choice(rgb_colors))
    tim.forward(50)

    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


sc = t.Screen()
sc.exitonclick()
