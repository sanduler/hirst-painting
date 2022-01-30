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
# create an object from turtle class
arrow = a.Turtle()
# change the shape for the turtle to triangle
arrow.shape("triangle")
# change the shape for the turtle
arrow.shapesize(.5, .5, 0)
# set the speed of the movement of the turtle
arrow.speed("slow")
# set the colormode
a.colormode(255)

# change the starting position of the turtle
y_counter = -200
# pickup the pen so it does not draw on the screen
arrow.penup()
# move the location to the start location
arrow.goto(-250, y_counter)


def dot():
    arrow.penup()
    arrow.forward(25)
    arrow.dot(20, random.choice(color_list))
    arrow.penup()
    arrow.forward(25)


# use an outer range to increment the location accouting for the rows
for a in range(10):
    # use the inner range to increment the movement for moving forward and creating a dot
    for i in range(10):
        dot()
    # increment the location of the y-axis upwards by 50
    y_counter += 50
    # pick up the pen so it does not draw on the screen
    arrow.penup()
    # go to the incremented position
    arrow.goto(-250, y_counter)

# screen stays on
screen = a.Screen()
# screen exits on click
screen.exitonclick()
