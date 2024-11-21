import turtle

def setup_turtle():
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Octagonal Spiral Group 7")
    t = turtle.Turtle()
    t.speed(1)  
    t.hideturtle()
    return t, screen

def draw_spiral():
    t, screen = setup_turtle()
    colors = ["yellow", "blue", "red", "purple", "orange", "green"]
    color_index = 0

    segments_per_cycle = 8
    complete_cycles = 4
    extra_segments = 5
    total_segments = (complete_cycles * segments_per_cycle) + extra_segments

    start_size = 15  
    max_size = 200  
    start_pen = 2  
    max_pen = 25  

    t.penup()
    t.goto(-start_size / 2, 0)  
    t.setheading(0)  
    t.pendown()
    size_growth = (max_size - start_size) / total_segments
    pen_growth = (max_pen - start_pen) / total_segments

    for segment in range(total_segments):
        current_size = start_size + (segment * size_growth)
        current_pen = start_pen + (segment * pen_growth)
        t.pensize(current_pen)
        t.pencolor(colors[color_index % len(colors)])
        t.forward(current_size)
        t.left(45)

        color_index += 1

    screen.mainloop()

if __name__ == "__main__":
    draw_spiral()
