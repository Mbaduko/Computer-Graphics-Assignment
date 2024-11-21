import turtle

# Set up the screen
screen = turtle.Screen()

screen.setup(width=600, height=300)
screen.bgcolor("blue")  
t = turtle.Turtle()
t.hideturtle()  
t.speed(0)      

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

t.penup()
t.goto(0, 0)  # Move to center
t.color("white")  
t.write("Welcome to  UR CST", align="center", font=("Arial", 24, "bold"))  

# Finish the drawing
turtle.done()