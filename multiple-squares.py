import turtle

# --- Setup ---
screen = turtle.Screen() # Creates the screen
screen.bgcolor("black") # Sets the screen's background colour
screen.title("Python Turtle Demo") # You can set the name of the screen

my_turtle = turtle.Turtle() # Create your turtle
my_turtle.speed(6)  # Set speed: 1 = slowest, 10 = fastest, 0 = instant
my_turtle.pensize(2) # Set the thickness of the pen line
my_turtle.pencolor("cyan") # Set the colour of the turtle's lines

my_turtle.penup() # Lift the pen up, so the turtle does not draw a line
my_turtle.goto(-200, 100) # Tell the turtle to go to a specific coordinate position

# Draw 3 squares
for k in range(3):
    my_turtle.pendown() # Put the pen down so that turtle can draw a line
    # Draw a square
    for i in range(4):
        my_turtle.forward(100)
        my_turtle.right(90)
    my_turtle.penup()
    my_turtle.forward(150)

turtle.done()
