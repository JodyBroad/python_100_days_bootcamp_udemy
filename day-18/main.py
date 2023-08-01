from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("DarkOrchid")

# draw a square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# draw a dashed line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# draw different shapes in random colours

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)


# random walk

tim.pen(pensize=10)
tim.speed("fastest")
directions = [0, 90, 180, 270]

def random_walk(number_of_stops):
    for i in range(number_of_stops):
        tim.color(random.choice(colours))
        tim.forward(30)
        tim.setheading(random.choice(directions))

random_walk(200)

# keep this at the bottom so we can view the results
screen = Screen()
screen.exitonclick()
