import turtle
import random
import math

# Set up the screen
wn = turtle.Screen()
wn.title("Gun Firing Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)

# Create the gun
gun = turtle.Turtle()
gun.color("white")
gun.shape("square")
gun.shapesize(stretch_wid=1, stretch_len=5)
gun.penup()
gun.goto(0, -250)
gun_speed = 20

# Create a bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.shapesize(stretch_wid=0.5, stretch_len=0.5)
bullet.hideturtle()
bullet_speed = 20
bullet_state = "ready"

# Create a target
target = turtle.Turtle()
target.color("red")
target.shape("circle")
target.penup()
target.speed(0)
target.shapesize(stretch_wid=1, stretch_len=1)
target.goto(random.randint(-280, 280), random.randint(100, 250))
target_speed = 2

# Functions
def move_left():
    x = gun.xcor()
    x -= gun_speed
    if x < -280:
        x = -280
    gun.setx(x)

def move_right():
    x = gun.xcor()
    x += gun_speed
    if x > 280:
        x = 280
    gun.setx(x)

def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        x = gun.xcor()
        y = gun.ycor() + 10
        bullet.goto(x, y)
        bullet.showturtle()

def is_collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

# Keyboard bindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(move_left, "a")
wn.onkeypress(move_right, "d")
wn.onkeypress(fire_bullet, "space")

# Main game loop
while True:
    wn.update()

    # Move the target
    target.setx(target.xcor() + target_speed)

    # Move the target back and change direction if it hits the wall
    if target.xcor() > 280:
        target_speed *= -1
        target.sety(target.ycor() - 40)

    if target.xcor() < -280:
        target_speed *= -1
        target.sety(target.ycor() - 40)

    # Move the bullet
    if bullet_state == "fire":
        y = bullet.ycor() + bullet_speed
        bullet.sety(y)

    # Check for bullet collision with target
    if is_collision(bullet, target):
        bullet.hideturtle()
        bullet_state = "ready"
        bullet.goto(0, -400)
        target.goto(random.randint(-280, 280), random.randint(100, 250))

    # Check for bullet reaching the top
    if bullet.ycor() > 290:
        bullet.hideturtle()
        bullet_state = "ready"

wn.mainloop()
