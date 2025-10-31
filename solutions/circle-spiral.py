import turtle

# --- Setup ---
screen = turtle.Screen() # Creates the screen
screen.bgcolor("black") # Sets the screen's background colour
screen.title("Python Turtle Demo") # You can set the name of the screen

my_turtle = turtle.Turtle() # Create your turtle
my_turtle.speed(4)  # Set speed: 1 = slowest, 10 = fastest, 0 = instant
my_turtle.pensize(2) # Set the thickness of the pen line

colours = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(12):
    my_turtle.pencolor(colours[i%6])
    my_turtle.circle(50)
    my_turtle.right(30)

turtle.done()
