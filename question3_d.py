import turtle

def setup_turtle():
    """
    Initialize and configure the turtle
    """
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Octagonal Spiral")

    t = turtle.Turtle()
    t.speed(1)  # Fastest speed
    t.hideturtle()
    return t, screen

def draw_spiral():
    """
    Draw an octagonal spiral starting horizontally and ending at the top
    """
    t, screen = setup_turtle()

    # Colors for the spiral
    colors = ["yellow", "blue", "red", "purple", "orange", "green"]
    color_index = 0

    # Spiral parameters
    segments_per_cycle = 8
    complete_cycles = 4
    extra_segments = 5
    total_segments = (complete_cycles * segments_per_cycle) + extra_segments

    # Starting parameters
    start_size = 15  # Starting size
    max_size = 200  # Maximum size
    start_pen = 2  # Starting pen size
    max_pen = 25  # Maximum pen thickness

    # Center the turtle and point it right (horizontal)
    t.penup()
    t.goto(-start_size / 2, 0)  # Start slightly left of center
    t.setheading(0)  # Point right
    t.pendown()

    # Calculate growth per segment
    size_growth = (max_size - start_size) / total_segments
    pen_growth = (max_pen - start_pen) / total_segments

    # Draw the spiral
    for segment in range(total_segments):
        # Calculate current size and pen thickness
        current_size = start_size + (segment * size_growth)
        current_pen = start_pen + (segment * pen_growth)

        # Set pen properties
        t.pensize(current_pen)
        t.pencolor(colors[color_index % len(colors)])

        # Draw segment
        t.forward(current_size)

        # Turn exactly 45 degrees for perfect octagon
        t.left(45)

        # Update color
        color_index += 1

    screen.mainloop()

if __name__ == "__main__":
    draw_spiral()
