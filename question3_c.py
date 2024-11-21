import turtle
import math

# Set up the screen and turtle
screen = turtle.Screen()
screen.title('Star Fractal - PythonTurtle.Academy')
screen.setup(800, 800)  # Set up a smaller screen size for better visibility
screen.screensize(600, 600)  # Adjust the drawing area size to fit the fractal
screen.tracer(0, 1)  # Set a small delay for visible drawing progress
turtle.hideturtle()
turtle.speed(0)

def star(x, y, length, penc, fillc):
    turtle.up()
    turtle.goto(x, y)
    turtle.seth(90)
    turtle.fd(length)
    turtle.seth(180 + 36 / 2)
    L = length * math.sin(36 * math.pi / 180) / math.sin(54 * math.pi / 180)
    turtle.seth(180 + 72)
    turtle.down()
    turtle.fillcolor(fillc)
    turtle.pencolor(penc)
    turtle.begin_fill()
    for _ in range(5):
        turtle.fd(L)
        turtle.right(72)
        turtle.fd(L)
        turtle.left(144)
    turtle.end_fill()

def star_fractal(x, y, length, penc, fillc, n):
    if n == 0:
        star(x, y, length, penc, fillc)
        return
    length2 = length / (1 + (math.sin(18 * math.pi / 180) + 1) / math.sin(54 * math.pi / 180))
    L = length - length2 - length2 * math.sin(18 * math.pi / 180) / math.sin(54 * math.pi / 180)
    for i in range(5):
        star_fractal(x + math.cos((90 + i * 72) * math.pi / 180) * (length - length2),
                     y + math.sin((90 + i * 72) * math.pi / 180) * (length - length2),
                     length2, penc, fillc, n - 1)

# Draw the star fractal with a smaller initial length to fit the screen
star_fractal(0, 0, 300, 'blue', 'blue', 3)  # Reduced length to 300
screen.update()

# Keep the window open
screen.mainloop()