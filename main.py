# import colorgram
#
# # create a new list to hold all the extracted colors from the image
# rgb_colors = []
#
# # find the picture in the img folder
# colors = colorgram.extract("./img/image.jpg", 30)
#
# # for loop to assign each of the rgb values to corresponding one
# for color in colors:
#     # red color
#     r = color.rgb.r
#     # green color
#     g = color.rgb.g
#     # blue color
#     b = color.rgb.b
#     # create the tuple
#     new_color = (r, g, b)
#     # append the new color to the list
#     rgb_colors.append(new_color)
#
# # print the color
# print(rgb_colors)

# Extracted color list from the code above

import turtle as a
import random

color_list = [(241, 222, 86), (35, 98, 185), (86, 174, 218), (169, 67, 37), (217, 158, 84), (187, 16, 34),
              (173, 49, 85), (78, 108, 210), (225, 57, 103), (161, 163, 23), (166, 27, 17), (75, 176, 77),
              (232, 70, 44), (225, 123, 172), (125, 198, 117), (20, 55, 146), (59, 119, 64), (118, 226, 184),
              (71, 30, 43), (135, 216, 233), (238, 158, 217), (41, 172, 183), (29, 41, 84), (242, 175, 152),
              (162, 165, 235), (90, 30, 22)]

arrow = a.Turtle()
arrow.shape("triangle")
arrow.shapesize(.5, .5, 0)
# arrow.position(100.00, 0.00)
arrow.speed("slow")
a.colormode(255)


# def ger_random_color():
#     length = len(color_list)
#     random.ran


def start(up):
    x = -200
    y = -200 + up
    arrow.penup()
    arrow.goto(x, y)
    arrow.pendown()


upward = 0

# for _ in range(20):
#     start(upward)
#     for i in range(10):
#         arrow.forward(15)
#         arrow.pen()
#         arrow.forward(5)
#         arrow.pendown()
#     upward += 20

for i in range(10):
    arrow.forward(15)
    arrow.dot(10, random.choice(color_list))
    arrow.penup()
    arrow.forward(5)
    arrow.pendown()

screen = a.Screen()
screen.exitonclick()
