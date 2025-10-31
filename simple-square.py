import turtle

# --- Setup ---
screen = turtle.Screen() # Creates the screen
screen.bgcolor("cyan") # Sets the screen's background colour
screen.title("Python Turtle Demo") # You can set the name of the screen

my_turtle = turtle.Turtle() # Create your turtle
my_turtle.speed(6)  # Set speed: 1 = slowest, 10 = fastest, 0 = instant
my_turtle.pensize(2) # Set the thickness of the pen line
my_turtle.pencolor("purple") # Set the colour of the turtle's lines

# Draw a square
for i in range(4):
    my_turtle.forward(100)   # move forward 100 units
    my_turtle.right(90)      # turn right 90 degrees

turtle.done() # Gets the screen to stay up / not close

