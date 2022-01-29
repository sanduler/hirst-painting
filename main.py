import colorgram

# create a new list to hold all the extracted colors from the image
rgb_colors = []

# find the picture in the img folder
colors = colorgram.extract("./img/image.jpg", 30)

# for loop to assign each of the rgb values to corresponding one
for color in colors:
    # red color
    r = color.rgb.r
    # green color
    g = color.rgb.g
    # blue color
    b = color.rgb.b
    # create the tuple
    new_color = (r, g, b)
    # append the new color to the list
    rgb_colors.append(new_color)

# print the color
print(rgb_colors)
