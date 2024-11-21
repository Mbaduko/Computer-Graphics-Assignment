import turtle

# Set up the screen
screen = turtle.Screen()
# screen.title("Group 9")  # Commented out because it's not supported in some environments
screen.setup(width=600, height=300)
screen.bgcolor("blue")  # Set the background color to blue

# Create a turtle for drawing
t = turtle.Turtle()
t.hideturtle()  # Hide the turtle for static drawing
t.speed(0)      # Set the fastest drawing speed

# Draw a blue rectangle (background already blue, so this is optional)
t.penup()
t.goto(-300, 150)  # Start at top left
t.pendown()
t.color("blue")
t.begin_fill()
for _ in range(2):
    t.forward(600)  # Width of the rectangle
    t.right(90)
    t.forward(300)  # Height of the rectangle
    t.right(90)
t.end_fill()

# Draw "Hello" in the center of the screen
t.penup()
t.goto(0, 0)  # Move to center
t.color("white")  # Set the text color to white
t.write("Welcome to  UR CST", align="center", font=("Arial", 24, "bold"))  # Write the word "Hello"

# Finish the drawing
turtle.done()