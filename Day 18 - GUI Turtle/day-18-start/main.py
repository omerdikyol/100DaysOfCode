import random
import turtle
from turtle import Turtle, Screen
#from turtle import *  # Importing everything from module ( Not preferred )
#import turtle as t

tim = Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

#tim.shape("turtle")        # Changing the cursor shape
#tim.color("red")           # Changing the color
#tim.forward(100)
#tim.left(90)


# Turtle Challenge 1 - Draw a Square
# for i in range(4):
#     tim.forward(200)
#     tim.left(90)


# Turtle Challenge 2 - Draw a Dashed Line
# for i in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# Turtle Challenge 3 - Drawing Different Shapes
# colors = ["blue", "forest green", "goldenrod", "coral", "deep pink", "indigo", "black", "peach puff", "red", "yellow"]
# for i in range(4,11):
#     angle = 360/i
#     tim.color(random.choice(colors))
#     for j in range(i):
#         tim.forward(100)
#         tim.right(angle)

# Turtle Challenge 4 - Generate a random walk with random color
# colors = ["blue", "forest green", "goldenrod", "coral", "deep pink", "indigo", "black", "peach puff", "red", "yellow"]
# angles = [90,180,270]
# tim.width(4)
# tim.speed(0)
# for i in range(200):
#     #tim.color(random.choice(colors))              # Old way
#     tim.color(random_color())
#     tim.forward(20)
#     tim.setheading(random.choice(angles))
#     tim.width(4+i/9)


# Tuple ==> Immutable ( Carved on stone ) Values on tuple is UNCHANGEABLE


# Turtle Challenge 5 - Draw a Spirograph
# def draw_spirograph(gap):
#     tim.speed(0)
#     for i in range( int(360/gap) ):
#         tim.color(random_color())
#         tim.circle(150)
#         tim.setheading(tim.heading() + gap)
# draw_spirograph(5)

screen = Screen()
screen.exitonclick()    #Opened tab won't disappear until we click on it