import turtle

# --- Setup ---
screen = turtle.Screen() # Creates the screen
screen.bgcolor("black") # Sets the screen's background colour
screen.title("Python Turtle Demo") # You can set the name of the screen

my_turtle = turtle.Turtle() # Create your turtle
my_turtle.speed(6)  # Set speed: 1 = slowest, 10 = fastest, 0 = instant
my_turtle.pensize(2) # Set the thickness of the pen line
my_turtle.pencolor("cyan") # Set the colour of the turtle's lines

# Define the movement functions
def move_forward():
    my_turtle.forward(10)

def move_backward():
    my_turtle.backward(10)

def turn_left():
    my_turtle.left(10)

def turn_right():
    my_turtle.right(10)

# Bind the keys to the functions
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

# Listen for key presses
screen.listen()

# Keep the window open
turtle.done()