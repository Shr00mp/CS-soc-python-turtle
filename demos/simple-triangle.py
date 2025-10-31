import turtle

# --- Setup ---
screen = turtle.Screen() # Creates the screen
screen.bgcolor("purple") # Sets the screen's background colour
screen.title("Python Turtle Demo") # You can set the name of the screen

my_turtle = turtle.Turtle() # Create your turtle
my_turtle.speed(6)  # Set speed: 1 = slowest, 10 = fastest, 0 = instant
my_turtle.pensize(5) # Set the thickness of the pen line
my_turtle.pencolor("cyan") # Set the colour of the turtle's lines

# Draw an equilateral triangle
for i in range (3):
    my_turtle.forward(100)
    my_turtle.left(120)

turtle.done()
