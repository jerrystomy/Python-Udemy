# import colorgram as cg
# def get_color():
"""To get the color list from the image colors"""
#     colors = cg.extract("image.jpg",30)
#     rgb_colors = []
#     for color in colors:
#         r = color.rgb.r
#         g = color.rgb.g
#         b = color.rgb.b
#         color_tup = (r, g, b)
#         rgb_colors.append(color_tup)
#     return rgb_colors
# color_list = get_color()

import turtle as tt
import random


tim = tt.Turtle()
tt.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(244, 145, 34), (236, 73, 37), (207, 66, 130), (189, 43, 87), (237, 214, 61), (221, 52, 23), (54, 76, 191), (81, 87, 214), (173, 24, 45), (41, 47, 163), (222, 105, 204), (207, 154, 23), (62, 156, 231), (194, 23, 19), (201, 208, 42), (38, 151, 213), (251, 243, 139), (239, 136, 243), (108, 184, 36), (13, 20, 112), (74, 142, 11), (187, 133, 253)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = tt.Screen()
screen.exitonclick()