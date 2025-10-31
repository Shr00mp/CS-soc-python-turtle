import turtle

# --- Setup ---
screen = turtle.Screen() # Creates the screen
screen.bgcolor("black") # Sets the screen's background colour
screen.title("Python Turtle Demo") # You can set the name of the screen

my_turtle = turtle.Turtle() # Create your turtle
my_turtle.speed(4)  # Set speed: 1 = slowest, 10 = fastest, 0 = instant
my_turtle.pensize(2) # Set the thickness of the pen line
my_turtle.pencolor("cyan") # Set the colour of the turtle's lines

# Draw a 5-pointed star
for _ in range(5):
    my_turtle.forward(200)
    my_turtle.right(144)

# Finish
turtle.done()