import turtle
import math
import random
from PIL import Image

def drawCircle(t, x, y, radius):
    circumference = 2.0 * math.pi * radius
    distance = circumference / 120.0
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    for i in range(120):
        t.forward(distance)
        t.left(3)


def kochsnowflake(t, level, length):
    if level == 0:
        t.forward(length)
    else:
        for angle in [60, -120, 60, 0]:
            kochsnowflake(t, level-1, length/3)
            t.left(angle)

def draw_koch_snowflake(level):
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-150, 90)
    t.pendown()
    for i in range(3):
        kochsnowflake(t, level, 300)
        t.right(120)
    turtle.done()

draw_koch_snowflake(2)

def mondrian_pattern(t, x, y, w, h, depth):
    if depth == 0:
        t.color(random_color())
        t.begin_fill()
        t.goto(x, y)
        t.goto(x + w, y)
        t.goto(x + w, y + h)
        t.goto(x, y + h)
        t.goto(x, y)
        t.end_fill()
    else:
        if w > h:
            split = random.randint(w//4, 3*w//4)
            mondrian_pattern(t, x, y, split, h, depth-1)
            mondrian_pattern(t, x+split, y, w-split, h, depth-1)
        else:
            split = random.randint(h//4, 3*h//4)
            mondrian_pattern(t, x, y, w, split, depth-1)
            mondrian_pattern(t, x, y+split, w, h-split, depth-1)

def random_color():
    colors = ["red", "blue", "yellow", "white", "black"]
    return random.choice(colors)

def draw_mondrian_pattern():
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, -200)
    t.pendown()
    mondrian_pattern(t, -200, -200, 400, 400, 4)
    turtle.done()

draw_mondrian_pattern()



def grayscale(pixel):
    red, green, blue = pixel
    gray = int(0.2989 * red + 0.5870 * green + 0.1140 * blue)
    return (gray, gray, gray)

def sepia(image):

    gray_image = image.convert('L')

    
    sepia_image = Image.new('RGB', image.size)


    for y in range(image.height):
        for x in range(image.width):
            pixel = gray_image.getpixel((x, y))
            r, g, b = pixel
            new_r = int(min(r * 1.2, 255))
            new_g = int(min(g * 1.1, 255))
            new_b = int(min(b * 0.9, 255))
            sepia_pixel = (new_r, new_g, new_b)
            sepia_image.putpixel((x, y), sepia_pixel)

    return sepia_image


def enlarge(image, factor):
   
    width, height = image.size
    

    new_width, new_height = width * factor, height * factor
    new_image = Image.new(mode="RGB", size=(new_width, new_height))
    
    
    for y in range(height):
        for x in range(width):
            # Get the color of the pixel at (x, y) in the original image
            color = image.getpixel((x, y))
            
           
            for i in range(factor):
                for j in range(factor):
                    new_x, new_y = x * factor + i, y * factor + j
                    new_image.putpixel((new_x, new_y), color)
    
    return new_image
