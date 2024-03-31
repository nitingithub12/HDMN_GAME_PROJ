import turtle
import time
import random

# Set up the screen
wn = turtle.Screen()
wn.title("Car Race Game")
wn.setup(width=600, height=600)
wn.bgcolor("lightblue")
wn.tracer(0)  # Turns off screen updates

# Car
car = turtle.Turtle()
car.speed(0)
car.shape("square")
car.color("red")
car.shapesize(stretch_wid=1, stretch_len=2)  # Make car longer
car.penup()
car.goto(0, -250)
car.direction = "stop"

# Obstacles
obstacles = []

def create_obstacle():
    obstacle = turtle.Turtle()
    obstacle.speed(0)
    obstacle.shape("square")
    obstacle.color("black")
    obstacle.shapesize(stretch_wid=1, stretch_len=random.randint(1, 4))
    obstacle.penup()
    x = random.randint(-280, 280)
    y = random.randint(300, 400)
    obstacle.goto(x, y)
    obstacles.append(obstacle)

def move_obstacles():
    for obstacle in obstacles:
        y = obstacle.ycor()
        y -= 2
        obstacle.sety(y)

        # Check for collision with car
        if obstacle.distance(car) < 20:
            return True

        # Check if obstacle is out of screen
        if y < -300:
            x = random.randint(-280, 280)
            y = random.randint(300, 400)
            obstacle.goto(x, y)

# Keyboard controls
def go_left():
    x = car.xcor()
    x -= 20
    if x < -280:
        x = -280
    car.setx(x)

def go_right():
    x = car.xcor()
    x += 20
    if x > 280:
        x = 280
    car.setx(x)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
while True:
    wn.update()

    # Create obstacles
    if len(obstacles) < 10:
        create_obstacle()

    # Move obstacles
    if move_obstacles():
        break

    time.sleep(0.01)

# Game over message
game_over = turtle.Turtle()
game_over.speed(0)
game_over.color("red")
game_over.penup()
game_over.hideturtle()
game_over.goto(0, 0)
game_over.write("Game Over", align="center", font=("Courier", 24, "normal"))

wn.mainloop
