import turtle
import random
import time

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Coin Collector Game")

player = turtle.Turtle()
player.shape("turtle")
player.color("cyan")
player.penup()
player.speed(0)

# Create the coin turtle
coin = turtle.Turtle()
coin.shape("circle")
coin.color("yellow")
coin.penup()
coin.speed(0)
coin.shapesize(0.5, 0.5)  # smaller dot

# Game variables
score = 0
coins_to_collect = 5
start_time = None

# Functions to move the player
def go_up():
    player.setheading(90)
    player.forward(20)

def go_down():
    player.setheading(270)
    player.forward(20)

def go_left():
    player.setheading(180)
    player.forward(20)

def go_right():
    player.setheading(0)
    player.forward(20)

# Function for placing the coin randomly
def place_coin():
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    coin.goto(x, y)

# Function to check for collision with coin + end game
def check_collision():
    global score, start_time
    if player.distance(coin) < 20:  # collision threshold
        score += 1
        if score == 1:  # Start timer when first coin collected
            start_time = time.time()
        if score < coins_to_collect:
            place_coin()
        else:
            end_time = time.time()
            total_time = round(end_time - start_time, 2)
            screen.textinput("You Win!", f"You collected {coins_to_collect} coins in {total_time} seconds! Press OK to exit.")
            turtle.bye()  # close the game

# Keyboard bindings
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")


place_coin()  # place first coin

# Game loop
while True:
    screen.update()
    check_collision()
