import turtle, random

colors  = ["red","green","blue","orange","purple","yellow","black", "medium sea green","sienna","navy","gray","indigo","lavender","salmon","teal"]

screen = turtle.Screen()
screen.bgcolor("skyblue")

screen.register_shape("ship", ((-10, -10), (0, -5), (10, -10), (0, 10)))
screen.register_shape("rock1", ((-20, -16), (-21, 0), (-20, 18), \
                                (0, 27), (17, 15), (25, 0), (16, -15), (0, -21)))
screen.register_shape("rock2", ((-15, -10), (-16, 0), (-13, 12), \
                                (0, 19), (12, 10), (20, 0), (12, -10), (0, -13)))
screen.register_shape("rock3", ((-10, -5), (-12, 0), (-8, 8), (0, 13), \
                                (8, 6), (14, 0), (12, 0), (8, -6), (0, -7)))

screen.register_shape("bullet", ((-2, -4), (-2, 4), (2, 4), (2, -4)))

ship = turtle.Turtle()
ship.shape("ship")
ship.turtlesize(1.5,1.5,1.5)
ship.penup()
ship.speed(0)
ship.color("black")
ship.goto(0, 0)

bullet = turtle.Turtle()
bullet.shape("turtle")
bullet.penup()
bullet.speed(0)
bullet.color("red")
bullet.goto(-1000, 1000)

asteroids = []
for i in range(12):
    a = turtle.Turtle()
    a.penup()
    a.speed(0)
    a.shape("rock" + str(random.randint(1, 3)))
    color = random.choice(colors)
    a.color(color)
    a.goto(random.randint(-200, 200), random.randint(-200, 200))
    asteroids.append(a)

finished = False
def move():
    while not finished:
        for a in asteroids:
            a.goto(a.xcor()+random.randint(-50, 50), a.ycor()+random.randint(-50, 50))


def right():
    ship.right(10)


def left():
    ship.left(10)


def forward():
    ship.forward(5)
    for a in asteroids:
        if ship.distance(a) < 30:
            crash()
            break


def turnback():
    ship.right(180)


def fire():
    ammo = bullet.clone()
    ammo.goto(ship.position())
    ammo.showturtle()
    ammo.setheading(ship.heading())
    ammo.speed(4)
    for i in range(10):
        ammo.forward(10)
        for a in asteroids:
            if ammo.distance(a) < 20:
                a.hideturtle()
                a.goto(-1000, 1000)
                del a
                ammo.hideturtle()
                break
    ammo.speed(0)
    ammo.hideturtle()
    del ammo
    gameover()


def crash():
    global finished
    finished = True
    ship.hideturtle()
    ship.color("blue")
    ship.write("Ship Crashed! \n You Lose!", font=("helvetica 12", 50, "bold"))


def gameover():
    done = True
    for a in asteroids:
        if a.xcor() == -1000:
            done *= True
        else:
            done *= False
    if done == True:
        global finished
        finished = True
        turtle.color("red")
        turtle.write("Game Over! \n You Win!", font=("Arial", 30, "bold"))


screen.onkey(right, "Right")
screen.onkey(left, "Left")
screen.onkey(forward, "Up")
screen.onkey(turnback, "Down")
screen.onkey(fire, "a")
screen.onkey(move, "m")
screen.listen()

turtle.done()