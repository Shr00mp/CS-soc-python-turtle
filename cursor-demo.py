import turtle

# --- Setup ---
screen = turtle.Screen() # Creates the screen
screen.bgcolor("black") # Sets the screen's background colour
screen.title("Python Turtle Demo") # You can set the name of the screen

my_turtle = turtle.Turtle() # Create your turtle
my_turtle.speed(6)  # Set speed: 1 = slowest, 10 = fastest, 0 = instant
my_turtle.pensize(2) # Set the thickness of the pen line
my_turtle.pencolor("cyan") # Set the colour of the turtle's lines

# Function that moves the turtle to the clicked location
def move_to_click(x, y):
    my_turtle.goto(x, y)

# Every time you click your mouse, the move_to_click function is called
# The coordinates x, y are passed into your function so that your turtle can move there
turtle.onscreenclick(move_to_click)

# Define a function that makes the turtle follow the cursor
def drag(x, y):
    my_turtle.ondrag(None) # Temporarily disable the drag event to prevent multiple calls at once
    my_turtle.goto(x, y) # Move turtle
    my_turtle.ondrag(drag) # Re-enable the drag event

my_turtle.ondrag(drag) # When you click and drag the turtle, it will following your cursor

turtle.done()
